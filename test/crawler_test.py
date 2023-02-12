import sys
sys.path.insert(1, '../src/')

import unittest

from models.card import Card
from crawler.expansions import loadExpansions
from crawler.url_gen import buildURLs
from crawler.crawl import getPrices

class CrawlerTest(unittest.TestCase):
    #Note: The delta argument is to account for fluctuations in the price.
    #      Don't worry too much if this test fails. It's likely because of market fluctuations

    condition = "NM"
    language = "English"
    firstEd = True
    amount = 1
    price = 0.0
    loadExpansions()
    logfile = open("./crawlertestlog.txt", "w")

    def buildCard(self, name, version, rarity, expansion) -> Card:
        return Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price)

    def testCrawler1(self):
        name = "Tatsunoko"
        version = 0
        rarity = "Super Rare"
        expansion = "HISU"
        expected = 0.02
        delta = 0.10
        card = self.buildCard(name, version, rarity, expansion)

        prices = getPrices(buildURLs(card, self.logfile), self.logfile)
        self.assertFalse(prices == {}, "Prices is empty")
        self.assertAlmostEqual(prices['fromPrice'], expected, delta=delta)

    def testCrawler2(self):
        name = "Knightmare Unicorn"
        version = 1
        rarity = "Rare"
        expansion = "GEIM"
        expected = 0.02
        delta = 0.10
        card = self.buildCard(name, version, rarity, expansion)

        prices = getPrices(buildURLs(card, self.logfile), self.logfile)
        self.assertFalse(prices == {}, "Prices is empty")
        self.assertAlmostEqual(prices['fromPrice'], expected, delta=delta)

    def testCrawler3(self):
        name = "The Winged Dragon of Ra"
        version = 2
        rarity = "Ghost Rare"
        expansion = "LED7"
        expected = 139.99
        delta = 50
        card = self.buildCard(name, version, rarity, expansion)

        prices = getPrices(buildURLs(card, self.logfile), self.logfile)
        self.assertFalse(prices == {}, "Prices is empty")
        self.assertAlmostEqual(prices['fromPrice'], expected, delta=delta)


    def testError1(self):
        name = "Manju of the Ten Thousand Hands"
        version = 0
        rarity = "Common"
        expansion = "OP18"
        expected = 0.02
        delta = 0.10
        card = self.buildCard(name, version, rarity, expansion)

        prices = getPrices(buildURLs(card, self.logfile), self.logfile)
        self.assertFalse(prices == {}, "Prices is empty")
        self.assertAlmostEqual(prices['fromPrice'], expected, delta=delta)


if __name__ == "__main__":
    unittest.main()