from selenium.common.exceptions import ElementNotInteractableException
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

#note: scrolling doesn't seem to work well when desktop (macos) with the browser windows isn't the one being used (tested multiple times)

def click_button(thebutton):
	# thebutton.location_once_scrolled_into_view 
# 	time.sleep(5)#weird but necessary to access this "field" (?) and wait a second (for the page to actually scroll) for the button to actually be scrolled into view
# 	thebutton.location_once_scrolled_into_view 
# 	time.sleep(5) #twice because it failed somehow???
# 	thebutton.click()
	
	driver.execute_script("return arguments[0].scrollIntoView(true);", thebutton) #yet another method (this still doesn't work 100%...)
	#input("This is here as a manual pause lol")
	time.sleep(5)
	thebutton.click()
	# try:
# 		thebutton.click()
# 	except ElementNotInteractableException:
# 		time.sleep(5)
# 		thebutton.location_once_scrolled_into_view 
# 		time.sleep(5)
# 		thebutton.click()

# def make_dict_org_data(org_name, org_desc, org_stack):
# 	return {"name": org_name, "description": org_desc, "technologies": org_stack} 

options = Options()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(20) #timespan of 20 seconds for all actions i.e. wait this much time before giving up and throwing a tantrum >:(((

#go to the website

driver.get("https://summerofcode.withgoogle.com/programs/2022/organizations")

#first: get rid of the cookie thing that keeps screwing everything up
driver.find_element(By.CSS_SELECTOR, "#cookieBar .cookieBarConsentButton").click()


# org_grid = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"grid")) #keep trying for 10s or until found
# paginator = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"grid-paginator__top"))
next_button = driver.find_element(By.CSS_SELECTOR, ".grid-paginator__top .mat-paginator-navigation-next")
#print(next_button.get_attribute("class"))
orgs_dicts = []
temp_window = webdriver.Firefox(options=options) #opening org urls
time.sleep(5) #wait for everything to load

#all orgs
#this is basically a do-while loop
while True:
	orgs_list = driver.find_elements(By.CSS_SELECTOR, ".grid .card")
	
	for org in orgs_list:
		org_dict = {
			"name": org.find_element(By.CSS_SELECTOR, ".name").text,
			"description": org.find_element(By. CSS_SELECTOR, ".short-description").text,
			"technologies" : [],
			"tags": []
		}
		temp_window.get(org.find_element(By.CSS_SELECTOR, ".content").get_attribute("href"))
		time.sleep(10) #wait for new page to load
		org_dict["technologies"] = temp_window.find_element(By.CSS_SELECTOR, ".tech__content").text.split(", ")
		orgs_dicts.append(org_dict)
		#print(orgs_dicts)
	if not("disable" in next_button.get_attribute("class")):
		click_button(next_button)
	else:
		break
temp_window.quit()
#tag-by-tag idea: for each tag, click on it, go through all cards displayed
#yes this is very inefficient but oh well (i am doing this at 8:15 pm on tuesday)
tags_buttons_list = driver.find_elements(By.CSS_SELECTOR, ".mat-chip-list-wrapper .mat-chip")
del tags_buttons_list[0] #remove the "all" button
for a_button in tags_buttons_list:
	tag_name = a_button.text
	click_button(a_button)
	time.sleep(5) #just in case
	while True:
		orgs_list = driver.find_elements(By.CSS_SELECTOR, ".grid .card")
		for org in orgs_list:
			for orgdict in orgs_dicts:
				if orgdict["name"] == org.find_element(By.CSS_SELECTOR, ".name").text:
					orgdict["tags"].append(tag_name)
		if not("disable" in next_button.get_attribute("class")):
			click_button(next_button)
		else:
			break

	

#scraping work should be done now - now to just dump orgs_dicts to a json file
file = open("output.json", "w", encoding="utf-8")
json.dump(orgs_dicts, file, indent = 1)
file.close()
temp_window.quit()
driver.quit()