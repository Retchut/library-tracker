import sys
sys.path.insert(1, '../src/')

import unittest

from models.card import Card
from crawler.expansions import loadExpansions
from crawler.url_gen import buildURLs

# condition = "NM"
# language = "English"
# firstEd = True
# amount = 1
# price = 0.0

class URLTest(unittest.TestCase):

    condition = "NM"
    language = "English"
    firstEd = True
    amount = 1
    price = 0.0
    loadExpansions()
    
    def getFailureString(self, expected, returnedURLs):
        return "\n{0}\n not in \n{1}".format(expected, returnedURLs)

    def testSimpleOneWord1(self):
        name = "Tatsunoko"
        version = 0
        rarity = "Super Rare"
        expansion = "HISU"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Hidden-Summoners/Tatsunoko"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testSimpleOneWord2(self):
        name = "Zefraath"
        version = 0
        rarity = "Super Rare"
        expansion = "MACR"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Crisis/Zefraath"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testSimpleTwoWords(self):
        name = "Zefra Providence"
        version = 0
        rarity = "Rare"
        expansion = "MACR"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Crisis/Zefra-Providence"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testSimpleMultipleWords(self):
        name = "Oracle of Zefra"
        version = 0
        rarity = "Super Rare"
        expansion = "PEVO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Pendulum-Evolution/Oracle-of-Zefra"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testCommas(self):
        name = "Zefraniu, Secret of the Yang Zing"
        version = 0
        rarity = "Rare"
        expansion = "CROS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Crossed-Souls/Zefraniu-Secret-of-the-Yang-Zing"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))



    def testSlash(self):
        name = "D/D/D Supersight King Zero Maxwell"
        version = 0
        rarity = "Common"
        expansion = "LIOV"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Lightning-Overdrive/DDD-Supersight-King-Zero-Maxwell"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))



    def testEquals(self):
        name = "Damage = Reptile"
        version = 0
        rarity = "Rare"
        expansion = "ANGU"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Ancient-Guardians/Damage-Reptile"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testColon(self):
        name = "Number 39: Utopia"
        version = 0
        rarity = "Ultra Rare"
        expansion = "DUPO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Duel-Power/Number-39-Utopia"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))



    def testAmpersand(self):
        name = "Ghost Reaper & Winter Cherries"
        version = 0
        rarity = "Ultra Rare"
        expansion = "DUPO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Duel-Power/Ghost-Reaper-Winter-Cherries"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAt(self):
        name = "Bururu @Ignister"
        version = 0
        rarity = "Rare"
        expansion = "IGAS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Ignition-Assault/Bururu-Ignister"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testLotsOfSymbols(self):
        name = "Danger!? Tsuchinoko?"
        version = 0
        rarity = "Ultra Rare"
        expansion = "MP19"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/2019-Gold-Sarcophagus-Tin-Mega-Pack/Danger-Tsuchinoko"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testDash(self):
        name = "Blue-Eyes White Dragon"
        version = 0
        rarity = "Premium Gold Rare"
        expansion = "MAGO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Gold/Blue-Eyes-White-Dragon"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testDashWithSpace(self):
        name = "Abyss Actor - Superstar"
        version = 0
        rarity = "Secret Rare"
        expansion = "DESO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Destiny-Soldiers/Abyss-Actor-Superstar"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testParentheses1(self):
        name = "Knightmare Unicorn"
        version = 1
        rarity = "Rare"
        expansion = "GEIM"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Genesis-Impact/Knightmare-Unicorn-V1-Rare"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testParentheses2(self):
        name = "The Winged Dragon of Ra"
        version = 2
        rarity = "Ghost Rare"
        expansion = "LED7"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Legendary-Duelists-Rage-of-Ra/The-Winged-Dragon-of-Ra-V2-Ghost-Rare"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testQuotationMarks1(self):
        name = "\"A\" Cell Breeding Device"
        version = 0
        rarity = "Common"
        expansion = "FOTB"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Force-of-the-Breaker/A-Cell-Breeding-Device"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testQuotationMarks2(self):
        name = "\"A\" Cell Incubator"
        version = 0
        rarity = "Common"
        expansion = "GLAS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Gladiators-Assault/A-Cell-Incubator"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))

    def testApostrophe1(self):
        name = "Gravekeeper's Shaman"
        version = 0
        rarity = "Common"
        expansion = "SS01"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Speed-Duel-Starter-Decks-Destiny-Masters/Gravekeeper-s-Shaman"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testApostrophe2(self):
        name = "Vanity's Fiend"
        version = 0
        rarity = "Common"
        expansion = "SR06"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Structure-Deck-Lair-of-Darkness/Vanity-s-Fiend"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))



    def testAlternateRarities1(self):
        name = "Effect Veiler"
        version = 2
        rarity = "Ultimate Rare"
        expansion = "DREV"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Duelist-Revolution/Effect-Veiler-V-2"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAlternateRarities2(self):
        name = "Blue-Eyes White Dragon"
        version = 2
        rarity = "Ultimate Rare"
        expansion = "YSKR"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Starter-Deck-Kaiba-Reloaded/Blue-Eyes-White-Dragon-V-2"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAlternateRarities3(self):
        name = "Celestia, Lightsworn Angel"
        version = 2
        rarity = "Ultimate Rare"
        expansion = "LODT"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Light-of-Destruction/Celestia-Lightsworn-Angel-V-2-Ultimate-Rare"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAlternateRarities4(self):
        name = "Lightning Storm"
        version = 2
        rarity = "Prismatic Secret Rare"
        expansion = "IGAS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Ignition-Assault/Lightning-Storm-V-2-Prismatic-Secret-Rare"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError1(self):
        name = "Majesty's Fiend"
        version = 0
        rarity = "Rare"
        expansion = "MGED"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Gold-El-Dorado/Majestys-Fiend"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError2(self):
        name = "Vanity's Fiend"
        version = 0
        rarity = "Common"
        expansion = "SR06"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Structure-Deck-Lair-of-Darkness/Vanity-s-Fiend"

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price))
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))

if __name__ == "__main__":
    unittest.main()