from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import smtplib

import smtplib
import ssl
from email.message import EmailMessage
import keyboard

prev_HTML = " "

def chec_WebPage_First():
    global prev_HTML
    loginURL = '*****************'
    email = "*****************"
    password = "*****************"
    driver = webdriver.Chrome("*************ChromeDriver")
    driver.get(loginURL)
    
    time.sleep(2)

    email_in = driver.find_element(By.NAME, "email")
    pass_in = driver.find_element(By.NAME, "password")
    email_in.send_keys(email)
    pass_in.send_keys(password)

    driver.find_element(By.CLASS_NAME,"btn-lg").click()

    time.sleep(10)

    html = driver.page_source
    prev_HTML = html
    driver.quit


def chec_WebPage():
    global prev_HTML
    loginURL = '*****************'
    email = "*****************"
    password = "*****************"
    driver = webdriver.Chrome("*****************ChromeDriver")
    driver.get(loginURL)
    #badgeString = '<span class="small-view-btn">Available</span> <span class="badge badge-light small-view-btn ng-binding">0'


    time.sleep(10)

    email_in = driver.find_element(By.NAME, "email")
    pass_in = driver.find_element(By.NAME, "password")
    email_in.send_keys(email)
    pass_in.send_keys(password)

    driver.find_element(By.CLASS_NAME,"btn-lg").click()

    time.sleep(10)

    driver.find_element(By.CLASS_NAME,"btn-primary")

    html = driver.page_source
    time.sleep(10)
    driver.quit
    #print("html****************************************" + html)
    #print("prevhtml****************************************" + prev_HTML)
    print("length" + len(html))
    print("prevlength" + len(prev_HTML))
    if(html == prev_HTML):
        #print("no diff")
        prev_HTML = html
        return 0
    if(html != prev_HTML):
        #print("some diff")
        prev_HTML = html
        return 1
    
        
    

    
    
def emailUpdate():
    email_address = '*****************'
    email_password = '*****************'
    email_receiver = '*****************'
    
    subject = 'New Appointment Available!'
    body = """
    New Appointment Available!
    """
    em = EmailMessage()
    em['From'] = email_address
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, email_receiver, em.as_string())

    
    
answer = chec_WebPage()
print("Building Baseline")
time.sleep(15)
answer = chec_WebPage()
print("first answer: ", answer)
if answer == 1: 
    emailUpdate()
    print("Status Update email being sent")
if(answer == 0):
    print("No status Update")
    
time_end_loop = time.time() + 60 * 15
time_end = time.time() + 60 * 240
once = 0
 
while time.time() < time_end:
    
    if(once == 0):
        print("Starting wait for ",6," hours finishing at ", time.time() + 60 * 240)
        print("Checking every ",15,"min next update at ", time.time() + 60 * 15)
        print("Running")
    once = 1
     
    if keyboard.is_pressed('space'):
        print("program exited")
        exit() 
    
    if time.time() > time_end_loop:
        print("Its been ",15,"m checkup time")
        time_end_loop = time.time() + 60 * 15
        answer = chec_WebPage()
        print("answer: ", answer)
        if answer == 1:
            #emailUpdate()
            print("Status Update email being sent")
        if answer == 0:
            print("No status Update") 
        print("Running")
     
    
    