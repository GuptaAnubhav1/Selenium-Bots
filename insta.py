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

usrname=input("enter username: ")
passwrd=getpass.getpass() 

browser=webdriver.Chrome()                            
browser.get("https://www.instagram.com/?hl=en")                  

browser.maximize_window()                                

while(1):
	try:
		search=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")            
		search.send_keys(usrname)
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("Retry your username !!!")

while(1):
	try:
		search=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
		search.send_keys(passwrd)
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("wrong password !!!")

while(1):
	try:
		browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()
		break
	except:
		print ("1")         


code=input("enter code: ")

while(1):
	try:
		search=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input")
		search.send_keys(code)
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("wrong code !!!")

while(1):
	try:
		browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
		break
	except:
		print ("3")     

while(1):
	try:
		search=browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")     
		search.send_keys('dcuint')
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("Retrying writing text in search box !!!")   

while(1):
	try:
		link = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span").click()
		break
	except:
		print ("4")                  

while(1):
	try:
		link = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/div/span/span[1]/button").click()
		break
	except:
		print ("5")  

input("press enter to close window")
browser.close()              