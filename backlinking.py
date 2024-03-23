import mysql.connector
from mysql.connector.plugins import caching_sha2_password
from xml.etree.ElementInclude import include
from selenium.webdriver.common.action_chains import ActionChains
#from django.http import HttpResponse
from multiprocessing import Value
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import requests

#Database connection 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9743mani@999",
  database="mani"
)
mycursor = mydb.cursor()

browser=webdriver.Firefox()

with open(r'C:\Users\Manikanta-WD\Desktop\run\toupload1.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        row1_website = row[0]
        try:
            #mycursor.execute("SELECT * FROM website_data WHERE website='northernhaircare.com.au'")
            mycursor.execute("SELECT * FROM website_data WHERE website = '%s'" % row1_website)
            myresult = mycursor.fetchall()
            website_status = myresult[0][10]
            website_username = myresult[0][2]
            website_email = myresult[0][3]
            website_password = myresult[0][4]
            website_tags = myresult[0][5]
            website_title = myresult[0][6]
            website_small_disc = myresult[0][7]
            website_full_disc = myresult[0][8]
            website_img = myresult[0][9]
            
            print(website_status)
            
            #check for the website status / 1 for first time running 
            if website_status == '1':
               print("sucess")
               #Register A User
               browser.get('https://aibookmarking.com/register') 
               username = browser.find_element(By.NAME, "username") 
               email = browser.find_element(By.NAME, "email") 
               password = browser.find_element(By.NAME, "password")
               password_confirm = browser.find_element(By.NAME, "password_confirmation")

               username.send_keys(website_username)
               email.send_keys(website_email) 
               password.send_keys(website_password)   
               password_confirm.send_keys(website_password) 
               sleep(2)
               
               browser.find_element(By.NAME, "submit").click()
               sleep(2)

               #Register A User
               browser.get('https://dbookmarking.com/register') 
               username = browser.find_element(By.NAME, "username") 
               email = browser.find_element(By.NAME, "email") 
               password = browser.find_element(By.NAME, "password")
               password_confirm = browser.find_element(By.NAME, "password_confirmation")

               username.send_keys(website_username)
               email.send_keys(website_email)
               password.send_keys(website_password)    
               password_confirm.send_keys(website_password)
               sleep(2)

               browser.find_element(By.NAME, "submit").click()
               sleep(2)
               
               #update status of the website
               mycursor.execute("UPDATE website_data SET status = '0' WHERE website = '%s'" % row1_website)
               mydb.commit()
              
               
                
            else: #for second time 
                print("fail")
                
                browser.get('https://ourbookmarking.com/login') #Login A User
                username = browser.find_element(By.NAME, "username") 
                password = browser.find_element(By.NAME, "password")

                username.send_keys(website_username)
                sleep(1)
                password.send_keys(website_password)
                sleep(1)

                browser.find_element(By.NAME, "submit").click()
                sleep(2)

                
                url = browser.find_element(By.NAME, "url") 
                url.send_keys(row1_website)
                sleep(1)
                browser.find_element(By.NAME, "submit").click()
                sleep(3)


                articleTitle = browser.find_element(By.NAME, "articleTitle") 
                articleTitle.send_keys(website_title)
                sleep(1)
                select = Select(browser.find_element(By.NAME, "category"))
                select.select_by_value("News")
                sleep(1)


                #browser.find_element(By.ID,'text_to_score').send_keys(row1_website)
                textarea = browser.find_element(By.ID, "description")
                textarea.click()
                sleep(1)
                textarea = browser.find_element(By.ID, "description")
                textarea.send_keys(website_full_disc)
                sleep(2)

                tag = browser.find_element(By.NAME, "tag") 
                tag.send_keys(website_tags)
                sleep(1)

                browser.find_element(By.CLASS_NAME, "saveChanges").click()
                sleep(3)

                browser.find_element(By.XPATH, '//button[@class="btn btn-primary submit-story"]').click()
                
                print(browser.current_url)

                website1_final_URL = browser.current_url 
                sleep(5)
                
                browser.get('https://dbookmarking.com/login') #Login A User
                username = browser.find_element(By.NAME, "username") 
                password = browser.find_element(By.NAME, "password")

                username.send_keys(website_username)
                sleep(1)
                password.send_keys(website_password)
                sleep(1)

                browser.find_element(By.NAME, "submit").click()
                sleep(2)

                
                url = browser.find_element(By.NAME, "url") 
                url.send_keys(row1_website)
                sleep(1)
                browser.find_element(By.NAME, "submit").click()
                sleep(3)


                articleTitle = browser.find_element(By.NAME, "articleTitle") 
                articleTitle.send_keys(website_title)
                sleep(1)
                select = Select(browser.find_element(By.NAME, "category"))
                select.select_by_value("News")
                sleep(1)


                #browser.find_element(By.ID,'text_to_score').send_keys(row1_website)
                textarea = browser.find_element(By.ID, "description")
                textarea.click()
                sleep(1)
                textarea = browser.find_element(By.ID, "description")
                textarea.send_keys(website_full_disc)
                sleep(2)

                tag = browser.find_element(By.NAME, "tag") 
                tag.send_keys(website_tags)
                sleep(1)

                browser.find_element(By.CLASS_NAME, "saveChanges").click()
                sleep(3)

                browser.find_element(By.XPATH, '//button[@class="btn btn-primary submit-story"]').click()

                print(browser.current_url)

                website1_final_URL = browser.current_url 
                sleep(5)
            
        except:
                pass
        
        
  
  
  
  
  


  

  
