import concurrent.futures
import requests 
import random
import time

PROXY_LIST = [
    "209.127.138.225:7322",
    "23.229.101.68:8592",
    "45.155.70.67:8077",
    "23.236.168.58:8606",
    "209.127.165.140:7232",
    "45.154.56.94:7112",
    "185.242.92.230:8314",
    "45.57.225.71:9153",
    "138.128.121.117:9189",
    "209.127.127.58:7156"
]

TICKERS = [
    'FB',
    'CLOV',
    'COIN',
    'TSLA',
    'AAPL'
]

proxy_username = "ajawmmid-dest"
proxy_password = "qenukfdjm32h"

def make_request(ticker):

    host_port = random.choice(PROXY_LIST)
    proxies = {
    "http": f"http://{proxy_username}:{proxy_password}@{host_port}",
    "https": f"http://{proxy_username}:{proxy_password}@{host_port}"
    }

    url = f'https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json?since=9999999999'
    r = requests.get(str(url),proxies=proxies)
    res = r.json()
    watchlist_count = res['symbol']['watchlist_count']
    print(f"{ticker}:{watchlist_count}")
    print(f"Time: {time.time()}")
    
    
while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(make_request,TICKERS)
    time_to_wait = 600 #in seconds 600s = 10m 
    time.sleep(time_to_wait)
