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


# In[ ]:


matches = re.findall(pattern, html, re.DOTALL)
conn = sqlite3.connect("historical_data.db")
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {company_name} (
    date TEXT PRIMARY KEY,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    adj_close REAL,
    volume INTEGER
);
"""
conn.execute(create_table_query)

for match in matches:
    date, open_, high, low, close, adj_close, volume = match
    volume = int(volume.replace(',', ''))
    insert_query = f"""
    INSERT OR IGNORE INTO {company_name} (date, open, high, low, close, adj_close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    conn.execute(insert_query, (date, open_, high, low, close, adj_close, volume))
conn.commit()
conn.close()


# In[ ]:




