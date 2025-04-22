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


df = pd.read_csv('stock.csv', na_values=['null'], index_col='date', parse_dates=True, infer_datetime_format=True)
df.isna().sum()
df.describe().T
df.corr()


# In[ ]:


df1 = df
df1['date'] = pd.to_datetime(df1.index)
stock_data = df1.set_index('date')
close_px = stock_data['adj_close']
open_px = stock_data['open']
high_px = stock_data['high']
low_px = stock_data['low']
plt.ylabel("prices")
plt.xlabel("Date")
plt.title(f"{company_name} Adjusted Close, Open, High, and Low Price over Time")
plt.plot(stock_data['adj_close'], label='Adjusted Closing Price', color='green')
plt.plot(stock_data['open'], label='Open', color='red')
plt.plot(stock_data['high'], label='High', color='yellow')
plt.plot(stock_data['low'], label='Low', color='cyan')
plt.legend(loc=2)
plt.show()


# In[ ]:


import nltk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

response = requests.get("https://finance.yahoo.com/quote/" + company_name)
html_source = str(response.content)
re_comments = '<p class=".*?">(.*?).<'
comments_list = re.findall(re_comments, html_source)
output_file = open("comments.txt", "w")
for comment in comments_list:
    print(comment, file=output_file)
output_file.close()

text = open("comments.txt", "r").read()
wc = WordCloud().generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()

