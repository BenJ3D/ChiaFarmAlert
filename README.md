<h1>Chia Farm Alert - Windows/Ubuntu</h1>

A Python 3 script to monitor your Chia farm and receive alerts via email when there are changes in the number of plots or wallet balance.

The script will also run in the background and update the information every 10 minutes. If there are changes in the number of plots or wallet balance, an email will be sent to the recipient email address.

UPDATE 2023-03-25
- Now is cross-plateform Windows-Linux(only tested on Ubuntu)
- Add parameters for change smtp and port for use any email address

Made with the help of chatGPT to iterate quickly !

![image](https://user-images.githubusercontent.com/49345674/220518241-df778eb5-147d-4e5f-9987-6be632fe4d9c.png) ![image](https://user-images.githubusercontent.com/49345674/220518418-7282bfd5-86a2-42af-a778-56d9e01eeccb.png)


<h2>UPDATE (February 24, 2023):</h2>
-Adding a parameter to set the delay between two updates

-Adding a parameter to define how often to send a report



<h2>Description</h2>
This script uses the Chia command-line interface to obtain the following information about your Chia farm:

-Number of plots

-Total Chia farmed

-Chia wallet balance

The script also provides a graphical user interface (GUI) with the following buttons:

`Refresh`: This button updates manually the GUI with the latest farm summary information.

`Send Email`: This button force sends an email to the recipient email address with the current farm summary information.

`Close`: This button closes the window and stops the script from running.

Dependencies
```Python3```
```pip```
```tkinter```
```tkinter.messagebox```
```tkinter.ttk```
```subprocess```
```smtplib```
```email.mime.text```
```schedule```

<h2>Gmail configuration</h2>

I strongly advise creating a new email address (Gmail is not mandatory, but you will need to modify the script accordingly to adapt the SMTP and port settings).

Configure your Gmail account to allow SMTP access: (Your gmail address must have the two-step validation active)

Go to your Google account settings and click on "Security" in the left-hand menu.
Scroll down to "Less secure app access" and turn it on.

Generate an app password by going to "Security" > "App passwords" and selecting "Mail" and your device.

Use the generated app password in the sender_password variable in the script.

<h2>Dependencies</h2>
You can download and install Python 3 from the official website: https://www.python.org/downloads/

https://www.dataquest.io/blog/install-pip-windows/  look that for install python and pip.

Make sure to add Python to your PATH environment variable during the installation process.

You can install the remaining dependencies using pip:

```pip install schedule```


<h2>Usage non-CLI</h2>

1- Download the ZIP archive by clicking on the "code" dropdown menu at the top of the page.

2- Extract the folder wherever you want.

3- Open the ChiaFarmAlert.py file with a text editor (like VSCode, it looks nicer that way :)) and update the email information at the beginning of the script with your own email, password, and recipient email address.
```
sender_email = "your-email@gmail.com"
sender_password = "your-email-password"
receiver_email = "recipient-email@gmail.com"
```


And if you want set delays :
```
send_a_control_email_every_n_hours = 24     # 0 for disable, sent summary mail to verify that everything is working correctly
refresh_delay_in_minutes = 10               # The time in minutes when the script refreshes the Chia data   
```

4- Configure your Gmail address that you will have created for this purpose (see below, you will also need to generate an application password from your Google account associated with this Gmail address).

<h2>Usage CLI</h2>
1. Clone the repository:

```git clone git@github.com:BenJ3D/ChiaFarmAlert.git```

2. Open the file `chia-farm-alert.py` in your favorite text editor.
3. Update the email information at the beginning of the script with your own email/smtp/port/password, and recipient email address.
```
sender_email = "your-email@mail.com"
sender_smtp = 'smtp.mail.com'
sender_smtp_port = 587
sender_password = "your-email-password"

receiver_email = "recipient-email@gmail.com"
```

And if you want set delays :
```
send_a_control_email_every_n_hours = 24     # 0 for disable, sent summary mail to verify that everything is working correctly
refresh_delay_in_minutes = 10               # The time in minutes when the script refreshes the Chia data   
```



<h2>Run the script:</h2>

In terminal :
```python3 chia-farm-alert.py```

Or Launch the script by right-clicking on it and selecting "Open with Python 3.10".

At startup, you should receive two emails indicating the number of plots and the wallet balance, which means everything is working correctly.

The script will open a window that shows the number of plots, wallet balance, and total Chia farmed. 

You can click the "Refresh" button to update the information, the "Send Email" button to send an email with the current information, and the "Close" button to close the window.

The script will also run in the background and update the information every 10 minutes. If there are changes in the number of plots or wallet balance, an email will be sent to the recipient email address.

<h3>Disclaimer</h3>
For the moment, the script is rudimentary:

-It does not work if Chia is not running or is no longer running // I will soon add error handling to send an email with the error

-The GUI interface is very slow.

When I have time, I will create a proper program with a user-friendly interface, compatible with both Linux and Windows.

This script is provided as-is, and the author is not responsible for any damages or losses that may occur as a result of using this script. The script should be used at your own risk.
