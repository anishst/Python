import os
from selenium import webdriver
from ATSFramework import EmailFL

driver = webdriver.Chrome()
url = 'https://www.eventbrite.com/o/capital-one-center-26413794281'
try:
    driver.get(url)
    if 'Sorry, there are no upcoming events' in driver.page_source:
        print("No Events found")
    else:
        print("Events found..sending email")
        EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], "Events found at capital one center",
                                 f"Check website https://www.eventbrite.com/o/capital-one-center-26413794281")
except:
    print(f"Something went wrong while checking {url} ")
    EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], " *** ERROR *** Events found at capital one center",
                             f" Something went wrong while Checking website https://www.eventbrite.com/o/capital-one-center-26413794281")
finally:
    driver.quit()