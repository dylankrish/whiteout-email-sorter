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

subject = "Iowa Ticket"
message = """
Hello, 

I am interested in buying your ticket. Please let me know if it is still available, and how low you are willing to sell it for.

Thanks,
Dylan Krishnan
"""

import time
import pyautogui

time.sleep(3)

# set pyautogui delay to 0.1 seconds

for email in email_list:
    pyautogui.click(177, 107)
    # type email
    pyautogui.typewrite(email)
    pyautogui.press("enter")
    pyautogui.press('tab')
    pyautogui.typewrite(subject)
    pyautogui.press('tab')
    # copy message to clipboard
    pyautogui.PAUSE = 0.2
    pyautogui.hotkey('command', 'v')
    pyautogui.delay = 0.1
    # press command enter
    pyautogui.hotkey('command', 'enter')