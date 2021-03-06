import time
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#for noticing stock is down
toaster = ToastNotifier() 

tickers = ['NFLX', 'AMZN', 'FB', 'GOOG', 'BRK-B', 'TSLA']
entry_prices = [770, 1500, 560, 870, 350, 510] #entry price at what price buy a stock in order

for ticker, entry_price in zip(tickers, entry_prices):
    url = requests.get(f'https://markets.businessinsider.com/stocks/{ticker}-stock')
    bs4 = BeautifulSoup(url.content, 'html.parser')

    #find the price of stock
    stock_price = bs4.find(class_="price-section__current-value").text

    #if ',' occurs in stock price
    if ',' in stock_price:
        stock_price = stock_price.replace(',', '')

    #from string to float
    stock_price = float(stock_price)

    if stock_price < entry_price:
        #notify user the stock is down
        toaster.show_toast(f'{ticker} stock', f'is down {stock_price}!')

    


