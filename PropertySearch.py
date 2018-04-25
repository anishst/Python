from selenium import webdriver
import time,csv, datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select


caps = DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings'] = True
driver = webdriver.Ie(capabilities=caps)
driver.implicitly_wait(10)

street = "Storm"
for i in range(1935,1937):
	try:
		driver.get("http://icare.fairfaxcounty.gov/ffxcare/search/commonsearch.aspx?mode=address")
		driver.find_element_by_id("inpNumber").send_keys(i)
		driver.find_element_by_id("inpStreet").send_keys(street)
		driver.find_element_by_id('btSearch').click()
		name = driver.find_element_by_xpath("//td[contains(text(),'Name')]/following-sibling::td")
		propAddress = driver.find_element_by_xpath("//td[contains(text(),'Property Location')]/following-sibling::td")
		# mailAddress = driver.find_element_by_xpath("//td[contains(text(),'Mailing Address')]/following-sibling::td")
		land = driver.find_element_by_xpath("//td[contains(text(),'Land Area (SQFT)')]/following-sibling::td")
		# print(name.text,"\t",address.text,"\t",land.text)
		# string1 = name.text + "\t" + propAddress.text + "\t" + mailAddress.text + "\t" + land.text
		string1 = name.text + "\t" + propAddress.text + "\t" + land.text
		driver.find_element_by_link_text("Values").click()
		at = driver.find_element_by_xpath("//td[contains(text(),'Current Assessed Total')]/following-sibling::td")
		# print(at.text)
		string1 = string1 + "\t" + str(at.text)
		print(string1)
	
	except Exception as e:
		print("no records for {} {}".format(i, street))



# driver.quit()

