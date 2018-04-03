from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

username = ''
password = ''
uri = "https://upassbc.translink.ca/"

#get chrome driver 
driver = webdriver.Chrome()
driver.get(uri)
driver.implicitly_wait(10)

#select the dropdown menu with text value "Simon Fraser University"
select = Select(driver.find_element_by_class_name('hasCustomSelect'))
select.select_by_value('sfu')

driver.find_element_by_id('goButton').click()

#Fill in credentials
username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')

username_input.send_keys(username)
password_input.send_keys(password)

driver.find_element_by_xpath("//input[@type='submit']").click()



