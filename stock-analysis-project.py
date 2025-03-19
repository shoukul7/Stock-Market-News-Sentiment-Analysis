#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Import Service class

driver_path = r"D:\chrome\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
s = Service(driver_path)
browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()

company_name = input("Enter the company name: ")
url = "https://finance.yahoo.com/quote/" + company_name + "/history/"
browser.get(url)
time.sleep(3)

