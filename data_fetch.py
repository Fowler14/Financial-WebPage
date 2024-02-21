import requests
import config

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=aapl&apikey={api_key}'

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=aapl&apikey={api_key}'

r = requests.get(url)
data = r.json()

print(data)

