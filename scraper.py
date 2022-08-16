from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import json
#for each org:
#	name
#	brief desc.
#	tech stack

# def make_dict_org_data(org_name, org_desc, org_stack):
# 	return {"name": org_name, "description": org_desc, "technologies": org_stack} 

options = Options()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10) #timespan of 10 seconds for all actions

#go to the website

driver.get("https://summerofcode.withgoogle.com/programs/2022/organizations")

# org_grid = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"grid")) #keep trying for 10s or until found
# paginator = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"grid-paginator__top"))
next_button = driver.find_element(By.CSS_SELECTOR, ".grid-paginator__top .mat-paginator-navigation-next")
print(next_button)
orgs_dicts = []
temp_window = webdriver.Firefox(options=options) #opening org urls
time.sleep(5) #wait for everything to load

for i in range(0,4):
	orgs_list = driver.find_elements(By.CSS_SELECTOR, ".grid .card")
	for org in orgs_list:
		org_dict = {
			"name": org.find_element(By.CSS_SELECTOR, ".name").text,
			"description": org.find_element(By. CSS_SELECTOR, ".short-description").text,
		}
		temp_window.get(org.find_element(By.CSS_SELECTOR, ".content").get_attribute("href"))
		time.sleep(5) #wait for new page to load
		org_dict["technologies"] = temp_window.find_element(By.CSS_SELECTOR, ".tech__content").text.split(", ")
		orgs_dicts.append(org_dict)
		#print(orgs_dicts)
	next_button.location_once_scrolled_into_view 
	time.sleep(5)#weird but necessary to check this "field" (?) and wait a second (for the page to actually scroll) for the button to actually be scrolled into view
	next_button.click()


#scraping work should be done now - now to just dump orgs_dicts to a json file
file = open("output.json", "w", encoding="utf-8")
json.dump(orgs_dicts, file)
file.close()
temp_window.quit()
driver.quit()