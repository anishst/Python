import os
import time

from selenium import webdriver
from ATSFramework import EmailFL

driver = webdriver.Chrome()
#  list of sites and xpath to latest article links
url = "https://www.bankrate.com/rates/interest-rates/prime-rate.aspx"
xpath = """//*[@id="csstyle"]/div[6]/main/div[1]/table/tbody/tr[1]/td[2]"""
current_rate = None

try:
    driver.get(url)
    print(url, xpath)
    time.sleep(2)
    table = driver.find_element_by_xpath(xpath)
    current_rate = float(table.text)
    print(f"Current WSJ Prime Rate: {table.text}")
except Exception as e:
    print(f"Something went wrong while scraping {url} {e} ")

if current_rate and current_rate <= 3.00:
    message = f"""
    <a href='https://www.bankrate.com/rates/interest-rates/prime-rate.aspx'>WSJ Prime Rate </a>  seems to have gone down.
    <p>Current WSJ Prime Rate: {table.text}</p>"""
    #  send email
    EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], "WSJ Mortgage Rate is at or below 3%", message)

driver.quit()