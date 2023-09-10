import re

# The text containing email addresses
text = """
dylankrish@gmail.com
dylan@dylankri.sh
promotions@dylankri.sh
krishnan.dylan@gmail.com
dak5839@psu.edu
"""

# Regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Find all email addresses in the text using the pattern
email_addresses = re.findall(email_pattern, text)

# Convert the list of email addresses to a Python list variable
email_list = list(email_addresses)

# Print the list of email addresses
print(email_list)

# email each email address
# if this doesn't work we can use pyautogui to do it

smtpserver = "smtp.office365.com"
smtpport = 587
from credentials import username,password

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


message = """
Hello, 

I am interested in buying your ticket. Please let me know if it is still available.

Thanks,
Dylan Krishnan
"""

for email in email_list:
    print("Sending email to " + email)
    msg = MIMEMultipart()
    msg['Subject'] = "Iowa Ticket"
    msg['From'] = username
    msg['To'] = email
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMT_SSL(smtpserver,smtpport)
    server.starttls()
    server.login(username,password)
    server.sendmail(username,email,msg.as_string())
    server.quit()

print("Emails sent successfully")