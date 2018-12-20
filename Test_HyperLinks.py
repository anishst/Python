"""This program tests the hyperlinks for a given page"""

from selenium import webdriver
import requests

website = 'https://www.section508.gov/about-us'

driver = webdriver.Chrome()
driver.get(website)

list_links = driver.find_elements_by_tag_name('a')

issue_links = [] 
for i in list_links:
	print(i.text) 					# print link text
	print(i.get_attribute('href')) 	# get urls
	try:
		r = requests.get(i.get_attribute('href'))
		print(r.status_code)		# print status code
		if r.status_code is not 200:
			issue_links.append(i.get_attribute('href'))
	except Exception as e:
		print(f"Unable to get status code for url: {i.get_attribute('href')}; {e}")
	print("*" * 50)

driver.quit()

# print list of links with issues
print(issue_links)




