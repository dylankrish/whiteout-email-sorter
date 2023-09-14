import re
import time

# The text containing email addresses
text = """
csb5623@psu.edu wants $175 for an Iowa (Sep 23) ticket.

cgi5056@psu.edu wants $270 for an Iowa (Sep 23) ticket.

gbv5034@psu.edu wants $475 for an Iowa (Sep 23) ticket.

Csm5658@psu.edu wants $375 for an Iowa (Sep 23) ticket.

cjs7477@psu.edu wants $450 for an Iowa (Sep 23) ticket.

akv5268@psu.edu wants $250 for an Iowa (Sep 23) ticket.

kbb5575@psu.edu wants $250 for an Iowa (Sep 23) ticket.

tjk5789@psu.edu wants $350 for an Iowa (Sep 23) ticket.

kcm5580@psu.edu wants $340 for an Iowa (Sep 23) ticket.

csm5658@psu.edu wants $300 for an Iowa (Sep 23) ticket.

tjk5789@psu.edu wants $350 for an Iowa (Sep 23) ticket.

avl6057@psu.edu wants $325 for an Iowa (Sep 23) ticket.

cag6228@psu.edu wants $350 for an Iowa (Sep 23) ticket.

rna5142@psu.edu wants $500 for an Iowa (Sep 23) ticket.

cmg6591@psu.edu wants $340 for an Iowa (Sep 23) ticket.

cak5904@psu.edu wants $300 for an Iowa (Sep 23) ticket.

spk5991@psu.edu wants $310 for an Iowa (Sep 23) ticket.

bcy5048@psu.edu wants $325 for an Iowa (Sep 23) ticket.

dsw5429@psu.edu wants $275 for an Iowa (Sep 23) ticket.

rpw5327@psu.edu wants $300 for an Iowa (Sep 23) ticket.

prc5095@psu.edu wants $300 for an Iowa (Sep 23) ticket.

xjd5036@psu.edu wants $300 for an Iowa (Sep 23) ticket.

vqs5312@psu.edu wants $325 for an Iowa (Sep 23) ticket.

yzp5220@psu.edu wants $300 for an Iowa (Sep 23) ticket.

axv5455@psu.edu wants $300 for an Iowa (Sep 23) ticket.

gdw5091@psu.edu wants $400 for an Iowa (Sep 23) ticket.

vmk5217@psu.edu wants $400 for an Iowa (Sep 23) ticket.

cvb5819@psu.edu wants $300 for an Iowa (Sep 23) ticket.

dbf5@pct.edu wants $300 for an Iowa (Sep 23) ticket.

mjl6891@psu.edu wants $345 for an Iowa (Sep 23) ticket.

cnn5104@psu.edu wants $500 for an Iowa (Sep 23) ticket.

jjd6021@psu.edu wants $250 for an Iowa (Sep 23) ticket.

kpp5506@psu.edu wants $450 for an Iowa (Sep 23) ticket.

jjd6021@psu.edu wants $300 for an Iowa (Sep 23) ticket.

ael5625@psu.edu wants $340 for an Iowa (Sep 23) ticket.

kmc7259@psu.edu wants $1000 for an Iowa (Sep 23) ticket.

jmg7674@psu.edu wants $500 for an Iowa (Sep 23) ticket.

baw5786@psu.edu wants $500 for an Iowa (Sep 23) ticket.

hbh5225@psu.edu wants $310 for an Iowa (Sep 23) ticket.

lmd5970@psu.edu wants $375 for an Iowa (Sep 23) ticket.

yab5063@psu.edu wants $400 for an Iowa (Sep 23) ticket.

cnc5478@psu.edu wants $400 for an Iowa (Sep 23) ticket. 

wbl5264@psu.edu wants $450 for an Iowa (Sep 23) ticket.

mjc7137@psu.edu wants $450 for an Iowa (Sep 23) ticket.

shw5143@psu.edu wants $350 for an Iowa (Sep 23) ticket.

mec6401@psu.edu wants $550 for an Iowa (Sep 23) ticket.

aww5483@psu.edu wants $400 for an Iowa (Sep 23) ticket.

smg6955@psu.edu wants $500 for an Iowa (Sep 23) ticket.

zvl5490@psu.edu wants $425 for an Iowa (Sep 23) ticket.

mjf6537@psu.edu wants $350 for an Iowa (Sep 23) ticket.

eer5276@psu.edu wants $175 for an Iowa (Sep 23) ticket.

vmk5217@psu.edu wants $480 for an Iowa (Sep 23) ticket.

mqh6100@psu.edu wants $550 for an Iowa (Sep 23) ticket.

enb5213@psu.edu wants $400 for an Iowa (Sep 23) ticket.

efm5427@psu.edu wants $320 for an Iowa (Sep 23) ticket.

jmm10420@psu.edu wants $375 for an Iowa (Sep 23) ticket.

knr5313@psu.edu wants $500 for an Iowa (Sep 23) ticket.

khd5077@psu.edu wants $500 for an Iowa (Sep 23) ticket.

aqj5361@psu.edu wants $375 for an Iowa (Sep 23) ticket.

erm5765@psu.edu wants $295 for an Iowa (Sep 23) ticket.

anb6230@psu.edu wants $500 for an Iowa (Sep 23) ticket.

dxp5503@psu.edu wants $420 for an Iowa (Sep 23) ticket.

pde5047@psu.edu wants $400 for an Iowa (Sep 23) ticket.

etd5107@psu.edu wants $400 for an Iowa (Sep 23) ticket.

pjk5630@psu.edu wants $350 for an Iowa (Sep 23) ticket.

lvp5393@psu.edu wants $500 for an Iowa (Sep 23) ticket.

egw5169@psu.edu wants $500 for an Iowa (Sep 23) ticket.

szk921@psu.edu wants $375 for an Iowa (Sep 23) ticket.

dsw5429@psu.edu wants $300 for an Iowa (Sep 23) ticket.

slm6158@psu.edu wants $600 for an Iowa (Sep 23) ticket.

dim5502@psu.edu wants $550 for an Iowa (Sep 23) ticket.

dim5502@psu.edu wants $525 for an Iowa (Sep 23) ticket.

dim5502@psu.edu wants $600 for an Iowa (Sep 23) ticket.

amb8788@psu.edu wants $350 for an Iowa (Sep 23) ticket.

enm5335@psu.edu wants $400 for an Iowa (Sep 23) ticket.

ajs9274@psu.edu wants $325 for an Iowa (Sep 23) ticket.

cjh6590@psu.edu wants $300 for an Iowa (Sep 23) ticket.

avc6581@psu.edu wants $600 for an Iowa (Sep 23) ticket.

gml5495@psu.edu wants $400 for an Iowa (Sep 23) ticket.

sls6866@psu.edu wants $1000 for an Iowa (Sep 23) ticket.

czh87@psu.edu wants $325 for an Iowa (Sep 23) ticket.

srm6237@psu.edu wants $400 for an Iowa (Sep 23) ticket.

sfc5856@psu.edu wants $1000 for an Iowa (Sep 23) ticket.

erm5765@psu.edu wants $700 for an Iowa (Sep 23) ticket.

lxk5378@psu.edu wants $400 for an Iowa (Sep 23) ticket.

bra5220@psu.edu wants $350 for an Iowa (Sep 23) ticket.

gml5495@psu.edu wants $295 for an Iowa (Sep 23) ticket.

frh5058@psu.edu wants $250 for an Iowa (Sep 23) ticket.

rne2@pct.edu wants $400 for an Iowa (Sep 23) ticket.

htm5123@psu.edu wants $325 for an Iowa (Sep 23) ticket. 

mjl6891@psu.edu wants $385 for an Iowa (Sep 23) ticket.
"""

# Regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Find all email addresses in the text using the pattern
email_addresses = re.findall(email_pattern, text)

# Convert the list of email addresses to a Python list variable
email_list = list(email_addresses)

# Print the list of email addresses
print(email_list)

# confirm with the user that they want to send emails
print("Are you sure you want to send emails to these addresses? (y/n)")
confirmation = input()
if confirmation != "y":
    exit()

# email each email address

smtpserver = "smtp.gmail.com"
smtpport = 587
from googlecredentials import username,password

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# TODO: Implement duplicate email checking

subject = "Iowa Ticket"
message = """
Hello, 

I am interested in buying your ticket. Please let me know if it is still available, and how much you are willing to sell it for.

Thanks,
Dylan Krishnan
PSU Email: dak5839@psu.edu
"""

for email in email_list:
    print("Sending email to " + email)
    msg = MIMEMultipart()
    msg['Subject'] = "Iowa Ticket"
    msg['From'] = username
    msg['To'] = email
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP(smtpserver,smtpport)
    server.starttls()
    server.login(username,password)
    server.sendmail(username,email,msg.as_string())
    server.quit()

print("Emails sent successfully")
