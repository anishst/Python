import os
from selenium import webdriver
from ATSFramework import EmailFL


def capital_one_center():
    driver = webdriver.Chrome()
    url = 'https://www.eventbrite.com/o/capital-one-center-26413794281'
    try:
        driver.get(url)
        if 'Sorry, there are no upcoming events' in driver.page_source:
            print("No Events found at capital one")
        else:
            print("Events found at capital one..sending email")
            EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], "Events found at capital one center",
                                     f"Check website https://www.eventbrite.com/o/capital-one-center-26413794281")
    except:
        print(f"Something went wrong while checking {url} ")
        EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], " *** ERROR *** Events found at capital one center",
                                 f" Something went wrong while Checking website https://www.eventbrite.com/o/capital-one-center-26413794281")
    finally:
        driver.quit()

def africal_american_museum():
    driver = webdriver.Chrome()
    url = 'https://event.etix.com/ticket/e/1018702/national-museum-of-african-american-history-and-culture-timedentry-passes-washington-national-museum-of-african-american-history-and-culture-general-public'
    try:
        driver.get(url)
        if 'No Passes Available' in driver.page_source:
            print("No tickets found at africal_american_museum")
        else:
            print("Tickets found..sending email")
            EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], "Tickets availalbe at Museum of African American History and Culture",
                                     f"Check website {url}")
    except:
        print(f"Something went wrong while checking {url} ")
        EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], " *** ERROR *** Museum of African American History and Culture ticket check",
                                 f" Something went wrong while Checking website {url}")
    finally:
        driver.quit()

capital_one_center()
africal_american_museum()