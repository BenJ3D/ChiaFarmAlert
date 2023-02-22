<h1>Chia Farm Alert</h1>
![image](https://user-images.githubusercontent.com/49345674/220518241-df778eb5-147d-4e5f-9987-6be632fe4d9c.png)

![image](https://user-images.githubusercontent.com/49345674/220518418-7282bfd5-86a2-42af-a778-56d9e01eeccb.png)

A Python 3 script to monitor your Chia farm and receive alerts via email when there are changes in the number of plots or wallet balance.

<h2>Description</h2>
This script uses the Chia command-line interface to obtain the following information about your Chia farm:

Number of plots
Total Chia farmed
Chia wallet balance
The script also provides a graphical user interface (GUI) with the following buttons:

`Refresh`: This button updates the GUI with the latest farm summary information.

`Send Email`: This button sends an email to the recipient email address with the current farm summary information.

`Close`: This button closes the window and stops the script from running.

The script will also run in the background and update the information every 10 minutes. If there are changes in the number of plots or wallet balance, an email will be sent to the recipient email address.


Dependencies
```Python 3```
```tkinter```
```tkinter.messagebox```
```tkinter.ttk```
```subprocess```
```smtplib```
```email.mime.text```
```schedule```
You can download and install Python 3 from the official website: https://www.python.org/downloads/

Make sure to add Python to your PATH environment variable during the installation process.

You can install the remaining dependencies using pip:

```pip install tkinter schedule```
<h2>Usage</h2>
1. Clone the repository:

```git clone https://github.com/<your-username>/chia-farm-alert.git```

2. Open the file `chia-farm-alert.py` in your favorite text editor.
3. Update the email information at the beginning of the script with your own email, password, and recipient email address.
```
sender_email = "your-email@gmail.com"
sender_password = "your-email-password"
receiver_email = "recipient-email@gmail.com"
```

5. Configure your Gmail account to allow SMTP access:
Go to your Google account settings and click on "Security" in the left-hand menu.
Scroll down to "Less secure app access" and turn it on.
Generate an app password by going to "Security" > "App passwords" and selecting "Mail" and your device.
Use the generated app password in the sender_password variable in the script.
Run the script:

```python3 chia-farm-alert.py```

The script will open a window that shows the number of plots, wallet balance, and total Chia farmed. You can click the "Refresh" button to update the information, the "Send Email" button to send an email with the current information, and the "Close" button to close the window.

The script will also run in the background and update the information every 10 minutes. If there are changes in the number of plots or wallet balance, an email will be sent to the recipient email address.

Disclaimer
This script is provided as-is, and the author is not responsible for any damages or losses that may occur as a result of using this script. The script should be used at your own risk.
