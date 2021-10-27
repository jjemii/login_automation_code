#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path_to_chromedriver = 'enter the path of chromedriver.exe' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://app.7mind.de/login'
browser.get(url)

username = browser.find_element_by_name("email")
password = browser.find_element_by_name("password")

username.send_keys("type the email of the user here")
password.send_keys("type password here")

browser.find_element_by_name("submit").click()

