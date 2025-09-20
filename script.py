import requests
import os
import csv
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

LIMIT = 1000
url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
response = requests.get(url)
tickers = []

data = response.json()
#print(data['next_url'])
for ticker in data['results']:
    tickers.append(ticker)

next_url = data['next_url']

while 'next_url' in data:
    print('requesting next page', data['next_url'])
    response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
    data = response.json()
    print(data)
    for ticker in data['results']:
        tickers.append(ticker)

print(f"Total tickers fetched: {len(tickers)}")
def run_stock_job():
# Write tickers to CSV file
    csv_filename = 'tickers.csv'
    fieldnames = ['ticker', 'name', 'market', 'locale', 'primary_exchange', 'type', 'active', 'currency_name', 'cik', 'composite_figi', 'share_class_figi', 'last_updated_utc']

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for ticker in tickers:
            # Ensure all fields are present, use empty string for missing fields
            row = {}
            for field in fieldnames:
                row[field] = ticker.get(field, '')
            writer.writerow(row)
        print(f"Ticker data written to {csv_filename}")

# Example ticker for reference
example_ticker = {'ticker': 'HTBK', 
                          'name': 'Heritage Commerce Corp',
                          'market': 'stocks', 
                          'locale': 'us', 
                          'primary_exchange': 'XNAS', 
                          'type': 'CS', 
                          'active': True, 
                          'currency_name': 'usd', 
                          'cik': '0001053352', 
                          'composite_figi': 'BBG000C48437', 
                          'share_class_figi': 'BBG001SBY8P0', 
                          'last_updated_utc': '2025-09-19T06:05:18.516616798Z'}

if __name__ == "__main__":
    run_stock_job()
    
# what if I close my laptop and python process is killed then its risky.
# so we need to run this in a background process.
#use cron to run this in a background process.

