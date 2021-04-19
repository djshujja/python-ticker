import concurrent.futures
import requests
import time

URLS = [
    'https://api.stocktwits.com/api/2/streams/symbol/FB.json?since=9999999999',
    'https://api.stocktwits.com/api/2/streams/symbol/CLOV.json?since=9999999999',
    'https://api.stocktwits.com/api/2/streams/symbol/COIN.json?since=9999999999',
    "https://api.stocktwits.com/api/2/streams/symbol/TSLA.json?since=9999999999",
    "https://api.stocktwits.com/api/2/streams/symbol/AAPL.json?since=9999999999"
]

def make_request(url):
    r = requests.get(str(url))
    res = r.json()
    watchlist_count = res['symbol']['watchlist_count']
    print(f"watchlist count = {watchlist_count}")
    
    
while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(make_request,URLS)
    time_to_wait = 5 #in seconds
    time.sleep(time_to_wait)