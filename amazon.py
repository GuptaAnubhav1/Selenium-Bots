import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import urllib.request
import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
import getpass

username=input("enter email: ")
password=getpass.getpass() 

browser=webdriver.Chrome()                            
browser.get("https://www.amazon.co.uk/")                  

browser.maximize_window()                                


while(1):
	try:
		search=browser.find_element_by_xpath("//*[@type='text']")     
		search.send_keys('Apple iPhone 11')
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("Retrying writing text in search box !!!")

while(1):
	try:
		link = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[4]/div[1]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
		break
	except:
		print ("Retrying")

while(1):
	try:
		browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[7]/div[5]/div/div/div/form/div/div/div/div/div[2]/div/div[13]/div[1]/span/span/span/input").click()
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a").click()
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a").click()
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		search=browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")           
		search.send_keys(username)
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		search=browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input")
		search.send_keys(password)
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("wrong password !!!")
while(1):
	try:
		browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input").click()
		break
	except:
		print ("Retrying !!!")   

input("press enter to close window")
browser.close()                     