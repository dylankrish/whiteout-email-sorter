import re
import time

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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

subject = "Iowa Ticket"
message = """
Hello, 

I am interested in buying your ticket. Please let me know if it is still available, and how low you are willing to sell it for.

Thanks,
Dylan Krishnan
"""

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://outlook.office365.com/mail/")

from credentials import username,password,totpsecret
import pyotp
import hashlib
useTOTP = True

# Login
# Wait for login page
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'loginfmt')))
# Type username
driver.find_element(By.NAME, 'loginfmt').send_keys(username + '\n')

# Send enter key
# driver.find_element(By.NAME, 'loginfmt').send_keys(u'\ue007')
# Wait for password page
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'passwd')))
# Type password
driver.find_element(By.NAME, 'passwd').send_keys(password)
time.sleep(1)
# Send enter key
driver.find_element(By.NAME, 'passwd').send_keys(u'\ue007')
if useTOTP:
    # Wait for totp page
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'otc')))
    # Create a TOTP object with the given secret
    totp = pyotp.TOTP(totpsecret, digits=6, digest=hashlib.sha1)
    # Get the current TOTP code
    totpcode = totp.now()
    # Type totp code
    driver.find_element(By.NAME, 'otc').send_keys(totpcode)
    # Send enter key
    driver.find_element(By.NAME, 'otc').send_keys(u'\ue007')
    # If the expected verification code is not entered, we need to try a different one
    # check for id 'ViewDetails' or the login page
    while True:
        # if the view details button is visible, we are on the login page
        if driver.find_elements(By.ID, 'ViewDetails'):
            raise Exception('You didn\'t enter an expected verification code. Please try again.')
        # if the view details button is not visible, we are on the mail page
        elif driver.find_elements(By.ID, 'id__174'):
            break
else:
    # wait for the mail page
    # TODO: send system notifications?
    print('Please type your 2FA code and continue.')
    while True:
        if driver.find_elements(By.ID, 'id__174'):
            break

for email in email_list:
    # click mail button
    driver.find_element(By.ID, 'id__174').click()
    # type email
    driver.find_element(By.CLASS_NAME, 'T6Va1 VbY1P EditorClass aoWYQ').send_keys(email)
    driver.find_element(By.ID, 'TextField326').send_keys(subject)
    driver.find_element(By.CLASS_NAME, 'dFCbN dnzWM dPKNh DziEn Z6_Ux').send_keys(message)
    # click send
    driver.find_element(By.CLASS_NAME, 'ms-Button ms-Button--primary ms-Button--hasMenu be51T root-425').click()