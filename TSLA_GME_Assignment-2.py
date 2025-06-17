"""
TSLA & GME Assignment Questions 1–6

Student: Luke Martin
Course: Data Science for Finance
Date: June 17, 2025
"""

import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Question 1: Extract TSLA Stock Data
# -----------------------------
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(start="2010-01-01", end="2025-06-17")
tesla_data.reset_index(inplace=True)
print("Question 1: TSLA Data (first 5 rows)")
print(tesla_data.head())

# -----------------------------
# Question 2: Extract TSLA Revenue Data
# -----------------------------
url_tsla = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_tsla = requests.get(url_tsla).text
soup_tsla = BeautifulSoup(html_tsla, "html.parser")
table_tsla = soup_tsla.find("table", {"class": "historical_data_table"})
rows_tsla = table_tsla.tbody.find_all("tr")

data_tsla = []
for row in rows_tsla:
    cols = row.find_all("td")
    qtr = cols[0].text
    rev = cols[1].text.strip().replace('$','').replace(',','')
    data_tsla.append((qtr, float(rev)))
tesla_revenue = pd.DataFrame(data_tsla, columns=["Quarter", "Revenue"])
print("\nQuestion 2: TSLA Revenue (last 5 rows)")
print(tesla_revenue.tail())

# -----------------------------
# Question 3: Extract GME Stock Data
# -----------------------------
gme = yf.Ticker("GME")
gme_data = gme.history(start="2002-01-01", end="2025-06-17")
gme_data.reset_index(inplace=True)
print("\nQuestion 3: GME Data (first 5 rows)")
print(gme_data.head())

# -----------------------------
# Question 4: Extract GME Revenue Data
# -----------------------------
url_gme = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_gme = requests.get(url_gme).text
soup_gme = BeautifulSoup(html_gme, "html.parser")
table_gme = soup_gme.find("table", {"class": "historical_data_table"})
rows_gme = table_gme.tbody.find_all("tr")

data_gme = []
for row in rows_gme:
    cols = row.find_all("td")
    qtr = cols[0].text
    rev = cols[1].text.strip().replace('$','').replace(',','')
    data_gme.append((qtr, float(rev)))
gme_revenue = pd.DataFrame(data_gme, columns=["Quarter", "Revenue"])
print("\nQuestion 4: GME Revenue (last 5 rows)")
print(gme_revenue.tail())

# -----------------------------
# Setup: Define make_graph function
# -----------------------------
def make_graph(df, date_col, price_col, title, save_as=None):
    plt.figure(figsize=(12,4))
    plt.plot(df[date_col], df[price_col])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    if save_as:
        plt.savefig(save_as, bbox_inches='tight')
        print(f"Graph saved as {save_as}")
    plt.show()

# -----------------------------
# Question 5: Plot Tesla Stock Graph
# -----------------------------
print("\nQuestion 5: Tesla Stock Graph")
make_graph(tesla_data, 'Date', 'Close', 'Tesla Stock Closing Prices (2010–2025)', save_as='tesla_stock_graph.png')

# -----------------------------
# Question 6: Plot GameStop Stock Graph
# -----------------------------
print("\nQuestion 6: GameStop Stock Graph")
make_graph(gme_data, 'Date', 'Close', 'GameStop Stock Closing Prices (2002–2025)', save_as='gme_stock_graph.png')
