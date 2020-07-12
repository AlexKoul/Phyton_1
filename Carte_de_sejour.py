#!/usr/bin/env python
# coding: utf-8

# In[19]:


from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import openpyxl
import smtplib
driver = webdriver.Chrome(executable_path=r'C:\Users\verbi\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(2)
driver.get("http://www.oise.gouv.fr/booking/create/33985")
elemCocher = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "condition")))
elemCooqies = driver.find_element_by_link_text('Accepter')
elemCooqies.click()
elemCocher.click()
nextButton = driver.find_element_by_class_name('Bbutton')
nextButton.click()
'''booking = driver.find_element_by_id('FormBookingCreate')'''
booking = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "FormBookingCreate")))
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
driver.implicitly_wait(1)
smtpObj.login('alexalexjoelpaul@gmail.com','Bbbbbbbb-1')
driver.implicitly_wait(1)
if (booking.text == "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement."):
    smtpObj.sendmail("alexalexjoelpaul@gmail.com","alexanderk2204@gmail.com","Don't worry be happy!")

else:
    smtpObj.sendmail("alexalexjoelpaul@gmail.com","alexanderk2204@gmail.com","Alarm!")
    
smtpObj.quit()
driver.close()

