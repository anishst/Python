from selenium import webdriver



driver = webdriver.Chrome()

#  list of sites and xpath to latest article links
blog_list = [
    "https://automationpanda.com, //article/a",
    "https://www.lambdatest.com/blog, //h2[@class='blog-titel']/a",
    "https://blog.gurock.com/, //h1[@class='entry-title']/a", # testrail
    "https://qxf2.com/blog/, //h2[@class='excerpt-title']/a"

]

for item in blog_list:

    url, xpath = item.split(',')
    print(url)
    driver.get(url)
    print(xpath)
    links = driver.find_elements_by_xpath(xpath)
    #  get link text
    print([link.text for link in links ])
    print([f"""<a href="{str(link.get_attribute('href'))}">{str(link.text)}</a>""" for link in links])
    # get url
    print([link.get_attribute('href') for link in links])


driver.quit()