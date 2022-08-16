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

#open file and prepare to write
file = open("output.json", "w", encoding="utf-8")
#go to the website

driver.get("https://summerofcode.withgoogle.com/programs/2022/organizations")

# org_grid = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"grid")) #keep trying for 10s or until found
# paginator = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"grid-paginator__top"))
next_button = driver.find_element(By.CSS_SELECTOR, ".grid-paginator__top .mat-paginator-navigation-next")
print(next_button)
orgs_dict = []
time.sleep(5) #wait for everything to load
for i in range(0,4):
	orgs_list = driver.find_elements(By.CSS_SELECTOR, ".grid .card")
	for org in orgs_list:
		pass	
	print(len(orgs_list))
	next_button.click() 
	
file.close()
#driver.quit()