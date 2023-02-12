import requests
from bs4 import BeautifulSoup
from re import compile
from datetime import datetime

CRAWL_LOGFILE = "./crawllog.txt"

def getPrices(urls : list) -> dict:
    logfile = open(CRAWL_LOGFILE, 'a+')
    now_time = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
    logfile.write("\n------------------------------\n" + now_time + "\n------------------------------\n")

    prices = dict()
    for url in urls:
        response = requests.get(url)
        resp_str = str(response.status_code) + "| "
        if(response.status_code != 200):
            resp_str += "Bad status while crawling" + url
        print(resp_str)
        logfile.write(resp_str)
        prices = parsePrices(response)
        if prices != {}:
            break
    if prices == {}:
        price_error = "Couldn't fetch prices for the provided urls:\n" + str(urls)
        print(price_error)
        logfile.write(price_error)
    logfile.close()
    return prices


def parsePrices(response : requests.models.Response) -> dict:

    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        infoContainer = soup.select_one('div.info-list-container')
        infoData = [info.text for info in infoContainer.select('dd.col-6.col-xl-7')]
    except AttributeError:
        return {}
    else:
        # no items found
        if infoData == []:
            return {}

        # # prices are in the form "X,YY €". After matching a string to a price using the following regex,
        # # we remove the last 2 characters, replace the comma with a dot, and convert the string to a float
        euroRegex = compile(r'[0-9]*\.[0-9]{1,2}\ €')
        poundRegex = compile(r'£[0-9]*\.[0-9]{1,2}')
        prices = []
        for priceString in infoData:
            priceString = priceString.replace(',', '.')
            if euroRegex.match(priceString):
                prices.append(float(priceString[:-2]))
            elif poundRegex.match(priceString):
                prices.append(float(priceString[1:]))

        try:
            return {
                'fromPrice' : prices[0],
                'trendPrice' : prices[1],
                'monthPrice' : prices[2],
                'weekPrice' : prices[3],
                'dayPrice' : prices[4]
            }
        except IndexError:
            print("Index error at", response.url)
            return {}