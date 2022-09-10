import requests
from bs4 import BeautifulSoup
from re import compile

def getPrices(urls : list) -> dict:
    prices = dict()
    for url in urls:
        response = requests.get(url)
        if(response.status_code != 200):
            print("Bad status while crawling", url)
        prices = parsePrices(response)
        if prices != {}:
            break
    return prices


def parsePrices(response : requests.models.Response) -> dict:

    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        infoContainer = soup.select_one('div.info-list-container')
        infoData = [info.text for info in infoContainer.select('dd.col-6.col-xl-7')]
    except AttributeError:
        print("Error fetching prices on", response.url)
        return {}
    else:
        # no items found
        if infoData == []:
            return {}

        # # prices are in the form "X,YY €". After matching a string to a price using the following regex,
        # # we remove the last 2 characters, replace the comma with a dot, and convert the string to a float
        priceRegex = compile(r'[0-9]*\,[0-9]{1,2}\ \€')
        prices = [float(priceString[:-2].replace(',', '.')) for priceString in infoData if priceRegex.match(priceString)]

        try:
            result = {
                'fromPrice' : prices[0],
                'trendPrice' : prices[1],
                'monthPrice' : prices[2],
                'weekPrice' : prices[3],
                'dayPrice' : prices[4]
            }
        except IndexError:
            print("Index error at", response.url)

        return result