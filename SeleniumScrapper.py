from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

loginURL = 'https://www.exmapleurl.com/login'

email = "*************"
password = "*************"


driver = webdriver.Chrome("Local Location")

driver.get(loginURL)

time.sleep(2)

email_in = driver.find_element(By.NAME, "email")
pass_in = driver.find_element(By.NAME, "password")
email_in.send_keys(email)
pass_in.send_keys(password)

driver.find_element(By.CLASS_NAME,"btn-lg").click()

time.sleep(20)

c = driver.find_element(By.CLASS_NAME,"btn-primary")
print(c)

#print("works")
htmls= driver.page_source
print(htmls)

driver.quit