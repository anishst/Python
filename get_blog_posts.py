import os
from selenium import webdriver
from ATSFramework import EmailFL

driver = webdriver.Chrome()
message = f"""Here is your Weekly Digest from Test Blogs. This was generated from a Python script:{os.path.basename(__file__)}<br/><ul>"""

#  list of sites and xpath to latest article links
blog_list = [
    "https://techbeacon.com/app-dev-testing, //h2[@class='article-title']/a",
    "https://automationpanda.com, //article/a",
    "https://www.lambdatest.com/blog, //h2[@class='blog-titel']/a",
    "https://blog.gurock.com/, //h1[@class='entry-title']/a", # testrail
    "https://qxf2.com/blog/, //h2[@class='excerpt-title']/a",
    "https://medium.com/better-programming, //a[@data-post-id]"

]

for item in blog_list:
    url, xpath = item.split(',')
    try:
        driver.get(url)
        links = driver.find_elements_by_xpath(xpath)
        message += f"{url}<ul>"
        for link in links:
            # print(link.get_attribute('href'))
            message += f"""<li style='margin-bottom:5px;'><a href="{link.get_attribute('href')}">{link.text}</a></li>"""
        message += "</ul>"
    except:
        print(f"Something went wrong while scraping {url} ")

print(message)

#  send email
EmailFL.send_email_gmail([os.getenv('GMAIL_ID')], "My Weekly Test Blog Digest", message)
driver.quit()