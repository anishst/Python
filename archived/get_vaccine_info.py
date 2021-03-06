import os
from selenium import webdriver
from ATSFramework import EmailFL

url = 'https://genesis.soc.texas.gov/files/accessibility/vaccineprovideraccessibilitydata.csv'

import pandas as pd
pd.set_option('display.max_colwidth', 0)

df = pd.read_csv(url)
df = df[df.COUNTY.isin(['Fort Bend'])]
df = df[df.CITY.isin(['Rosenberg', 'Sugar Land', 'SUGAR LAND'])]
df.sort_values(by=['CITY'], inplace=True)
print(df.head())

message = df.to_html()

#  send email
EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], "Rosenberg/Suguar Land Vaccine Info", message)
