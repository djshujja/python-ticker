import concurrent.futures
import requests 
# import grequests
import time

# URLS = [
#     'https://api.stocktwits.com/api/2/streams/symbol/FB.json?since=9999999999',
#     'https://api.stocktwits.com/api/2/streams/symbol/CLOV.json?since=9999999999',
#     'https://api.stocktwits.com/api/2/streams/symbol/COIN.json?since=9999999999',
#     "https://api.stocktwits.com/api/2/streams/symbol/TSLA.json?since=9999999999",
#     "https://api.stocktwits.com/api/2/streams/symbol/AAPL.json?since=9999999999"
# ]


TICKERS = [
    'FB',
    'CLOV',
    'COIN',
    'TSLA',
    'AAPL'
]


proxies = {
    "http": "http://ajawmmid-dest:qenukfdjm32h@209.127.138.225:7322",
    "https": "http://ajawmmid-dest:qenukfdjm32h@209.127.138.225:7322"
}

def make_request(ticker):
    url = f'https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json?since=9999999999'
    r = requests.get(str(url), proxies=proxies)
    res = r.json()
    watchlist_count = res['symbol']['watchlist_count']
    print(f"{ticker}:{watchlist_count}")
    print(f"Time: {time.time()}")
    print('---')


def make_ph():
    url = 'https://9gag.com/'
    r = requests.get(str(url),proxies=proxies)
    print(r.content)


for ticker in TICKERS:
    # make_ph(ticker)
    make_ph()

    
# while True:
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.map(make_request,TICKERS)
#     time_to_wait = 600 #in seconds 600s = 10m 
#     time.sleep(time_to_wait)
