import sys
import matplotlib.pyplot as plt
import requests
import time

def get_cgi_ticker():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GIB&interval=1min&apikey='
    r = requests.get(url).json()
    quotes = r['Time Series (1min)']
    return [price['1. open'] for time, price in quotes.items()]

while 1:
    data = get_cgi_ticker()
    plt.plot(data)
    plt.title("Current stock price: {}".format(data[0]),fontsize=50)
    plt.show()
    time.sleep(5)
