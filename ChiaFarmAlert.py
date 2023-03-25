import subprocess
import platform
import smtplib
from email.mime.text import MIMEText
import time
import schedule
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys

# Email information
sender_email = "your-email@mail.com"
sender_smtp = 'smtp.mail.com'
sender_smtp_port = 587
sender_password = "your-email-password"

receiver_email = "recipient-email@gmail.com"

# Function to send email

# Déterminer la plateforme
plat = platform.system()

# Exécuter la commande appropriée en fonction de la plateforme
if plat == 'Windows':
    command1 = 'powershell chia wallet show'
    command2 = 'powershell.exe chia farm summary'
    vshell = True
elif plat == 'Linux':
    command1 = ['chia', 'wallet', 'show']
    command2 = ['chia', 'farm', 'summary']
    vshell = False
else:
    raise OSError('Plateforme non prise en charge')

def send_email(subject, message):
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP(sender_smtp, sender_smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(e)

# Function to format HTML output
def format_html_output(output):
    # Find Total chia farmed and number of plots
    lines = output.split("\n")
    for line in lines:
        if "Total chia farmed:" in line:
            total_chia_farmed = line.split(": ")[1].strip()
        elif "Plot count for all harvesters:" in line:
            plot_count = line.split(": ")[1].strip()

    # Find Chia Wallet balance
    chia_wallet_balance = "N/A"
    chia_wallet_output = subprocess.check_output(command1, shell=vshell).decode()
    chia_wallet_lines = chia_wallet_output.split("\n")
    for i in range(len(chia_wallet_lines)):
        if "Chia Wallet:" in chia_wallet_lines[i]:
            for j in range(i+1, len(chia_wallet_lines)):
                if chia_wallet_lines[j].startswith("   -Total Balance:"):
                    chia_wallet_balance = chia_wallet_lines[j].split(":")[1].strip()
                    break
                elif chia_wallet_lines[j].startswith("Pool wallet:"):
                    break
            break

    # Format HTML output
    html_output = "<html><body style=\"font-family: Arial, sans-serif;\">"
    html_output += "<h2 style=\"color: #1f3864;\">Chia Farm Summary</h2>"
    html_output += "<p>Total chia farmed: <span style=\"color: #009a1e;\">{}</span></p>".format(total_chia_farmed)
    html_output += "<p>Number of plots: <span style=\"color: #009a1e;\">{}</span></p>".format(plot_count)
    html_output += "<p>Chia Wallet balance: <span style=\"color: #009a1e;\">{}</span></p>".format(chia_wallet_balance)
    html_output += "<p>Last updated at: {}</p>".format(time.ctime())
    html_output += "</body></html>"

    return html_output

# Function to update the window with the latest farm summary information
def update_window():
    try:
        # Run "Chia farm summary" command
        output = subprocess.check_output(command2, shell=vshell).decode()

        # Check if the command was successful
        if "No module named" in output:
            print("An error occurred while running the command")
        else:
            # Format HTML output
            html_output = format_html_output(output)

            # Find number of plots
            lines = output.split("\n")
            for line in lines:
                if "Plot count for all harvesters:" in line:
                    plot_count = line.split(": ")[1].strip()
                    break
            # Find Total chia farmed
            lines = output.split("\n")
            for line in lines:
                if "Total chia farmed:" in line:
                    total_chia_farmed = line.split(": ")[1].strip()
                    total_chia_value.config(text=total_chia_farmed)
                    break

            # Find Chia Wallet balance
            chia_wallet_balance = "N/A"
            chia_wallet_output = subprocess.check_output(command1, shell=vshell).decode()
            chia_wallet_lines = chia_wallet_output.split("\n")
            for i in range(len(chia_wallet_lines)):
                if "Chia Wallet:" in chia_wallet_lines[i]:
                    for j in range(i+1, len(chia_wallet_lines)):
                        if chia_wallet_lines[j].startswith("   -Total Balance:"):
                            chia_wallet_balance = chia_wallet_lines[j].split(":")[1].strip()
                            break
                        elif chia_wallet_lines[j].startswith("Pool wallet:"):
                            break
                    break

            # Check if plot count has changed
            if plot_count != num_plots_value["text"]:
                message = "Number of plots has changed! New value: " + plot_count
                send_email("Chia Plot Count Changed", message)

            # Check if Chia Wallet balance has changed
            if chia_wallet_balance != wallet_balance_value["text"]:
                message = "Chia Wallet balance has changed! New value: " + chia_wallet_balance
                send_email("Chia Wallet Balance Changed", message)

            # Update farm summary labels
            num_plots_value.config(text=plot_count)
            wallet_balance_value.config(text=chia_wallet_balance)

            # Get a reference to the farm summary label
            farm_summary = window.nametowidget("farm_summary")

            # Update farm summary label
            farm_summary.config(text=html_output)

    except Exception as e:
        print(e)



# Function to send email when the email button is clicked
def on_email_button_click():
    try:
        # Run "Chia farm summary" command
        output = subprocess.check_output(command2, shell=vshell).decode()

        # Check if the command was successful
        if "No module named" in output:
            print("An error occurred while running the command")
        else:
            # Format HTML output
            html_output = format_html_output(output)

            # Send email
            send_email("Chia Farm Summary", html_output)

    except Exception as e:
        print(e)

# Fonction pour fermer la fenêtre
def close_window():
 if messagebox.askokcancel("Quit", "Do you want to quit?"):
        global running
        running = False
        window.destroy()
        sys.exit()

# Create the window
window = tk.Tk()
window.title("Chia Farm Alert")
window.geometry("400x300")

running = True

# Bind the close event to close the program
window.protocol("WM_DELETE_WINDOW", close_window)

# Create the farm summary labels
num_plots_label = tk.Label(window, text="Number of plots: ")
num_plots_label.pack()
num_plots_value = tk.Label(window, text="N/A")
num_plots_value.pack()

wallet_balance_label = tk.Label(window, text="Wallet balance: ")
wallet_balance_label.pack()
wallet_balance_value = tk.Label(window, text="N/A")
wallet_balance_value.pack()

total_chia_label = tk.Label(window, text="Total Chia farmed: ")
total_chia_label.pack()
total_chia_value = tk.Label(window, text="N/A")
total_chia_value.pack()

# Create the style for the buttons
style = ttk.Style()
style.theme_use('default')
style.configure('Custom.TButton', font=('Arial', 12), background='#3CB26D', foreground='white')
style.map('Custom.TButton', foreground=[('active', 'white')], background=[('active', '#45D170')])

# Create the email button
email_button = ttk.Button(window, text="Send Email", style='Custom.TButton', command=on_email_button_click)
email_button.pack(pady=10)

# Create the refresh button
refresh_button = ttk.Button(window, text="Refresh", style='Custom.TButton', command=update_window)
refresh_button.pack(pady=10)

# Create the close button
close_button = ttk.Button(window, text="Close", style='Custom.TButton', command=close_window)
close_button.pack(pady=10)

# Schedule task to update the farm summary window every 10 minutes
schedule.every(10).minutes.do(update_window)

update_window()

while running:
    window.update()
    schedule.run_pending()
    time.sleep(1)
