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
    modifiers = "?minCondition=2"
    logfile = open("./urltestlog.txt", "w")
    
    def getFailureString(self, expected, returnedURLs):
        return "\n{0}\n not in \n{1}".format(expected, returnedURLs)

    def testSimpleOneWord1(self):
        name = "Tatsunoko"
        version = 0
        rarity = "Super Rare"
        expansion = "HISU"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Hidden-Summoners/Tatsunoko"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testSimpleOneWord2(self):
        name = "Zefraath"
        version = 0
        rarity = "Super Rare"
        expansion = "MACR"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Crisis/Zefraath"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testSimpleTwoWords(self):
        name = "Zefra Providence"
        version = 0
        rarity = "Rare"
        expansion = "MACR"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Crisis/Zefra-Providence"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testSimpleMultipleWords(self):
        name = "Oracle of Zefra"
        version = 0
        rarity = "Super Rare"
        expansion = "PEVO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Pendulum-Evolution/Oracle-of-Zefra"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testCommas(self):
        name = "Zefraniu, Secret of the Yang Zing"
        version = 0
        rarity = "Rare"
        expansion = "CROS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Crossed-Souls/Zefraniu-Secret-of-the-Yang-Zing"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))



    def testSlash(self):
        name = "D/D/D Supersight King Zero Maxwell"
        version = 0
        rarity = "Common"
        expansion = "LIOV"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Lightning-Overdrive/DDD-Supersight-King-Zero-Maxwell"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))



    def testEquals(self):
        name = "Damage = Reptile"
        version = 0
        rarity = "Rare"
        expansion = "ANGU"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Ancient-Guardians/Damage-Reptile"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testColon(self):
        name = "Number 39: Utopia"
        version = 0
        rarity = "Ultra Rare"
        expansion = "DUPO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Duel-Power/Number-39-Utopia"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))



    def testAmpersand(self):
        name = "Ghost Reaper & Winter Cherries"
        version = 0
        rarity = "Ultra Rare"
        expansion = "DUPO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Duel-Power/Ghost-Reaper-Winter-Cherries"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAt(self):
        name = "Bururu @Ignister"
        version = 0
        rarity = "Rare"
        expansion = "IGAS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Ignition-Assault/Bururu-Ignister"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testLotsOfSymbols(self):
        name = "Danger!? Tsuchinoko?"
        version = 0
        rarity = "Ultra Rare"
        expansion = "MP19"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/2019-Gold-Sarcophagus-Tin-Mega-Pack/Danger-Tsuchinoko"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testDash(self):
        name = "Blue-Eyes White Dragon"
        version = 0
        rarity = "Premium Gold Rare"
        expansion = "MAGO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Gold/Blue-Eyes-White-Dragon"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))

    def testDash2(self):
        name = "Gem-Knight Seraphinite"
        version = 0
        rarity = "Secret Rare"
        expansion = "SHVA"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Shadows-in-Valhalla/GemKnight-Seraphinite"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testDashWithSpace(self):
        name = "Abyss Actor - Superstar"
        version = 0
        rarity = "Secret Rare"
        expansion = "DESO"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Destiny-Soldiers/Abyss-Actor-Superstar"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testParentheses1(self):
        name = "Knightmare Unicorn"
        version = 1
        rarity = "Rare"
        expansion = "GEIM"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Genesis-Impact/Knightmare-Unicorn-V1-Rare"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testParentheses2(self):
        name = "The Winged Dragon of Ra"
        version = 2
        rarity = "Ghost Rare"
        expansion = "LED7"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Legendary-Duelists-Rage-of-Ra/The-Winged-Dragon-of-Ra-V2-Ghost-Rare"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testQuotationMarks1(self):
        name = "\"A\" Cell Breeding Device"
        version = 0
        rarity = "Common"
        expansion = "FOTB"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Force-of-the-Breaker/A-Cell-Breeding-Device"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testQuotationMarks2(self):
        name = "\"A\" Cell Incubator"
        version = 0
        rarity = "Common"
        expansion = "GLAS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Gladiators-Assault/A-Cell-Incubator"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))

    def testApostrophe1(self):
        name = "Gravekeeper's Shaman"
        version = 0
        rarity = "Common"
        expansion = "SS01"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Speed-Duel-Starter-Decks-Destiny-Masters/Gravekeeper-s-Shaman"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testApostrophe2(self):
        name = "Vanity's Fiend"
        version = 0
        rarity = "Common"
        expansion = "SR06"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Structure-Deck-Lair-of-Darkness/Vanity-s-Fiend"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testApostrophe3(self):
        name = "Majesty's Fiend"
        version = 0
        rarity = "Rare"
        expansion = "MGED"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Maximum-Gold-El-Dorado/Majestys-Fiend"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAlternateRarities1(self):
        name = "Effect Veiler"
        version = 2
        rarity = "Ultimate Rare"
        expansion = "DREV"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Duelist-Revolution/Effect-Veiler-V-2"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAlternateRarities2(self):
        name = "Blue-Eyes White Dragon"
        version = 2
        rarity = "Ultimate Rare"
        expansion = "YSKR"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Starter-Deck-Kaiba-Reloaded/Blue-Eyes-White-Dragon-V-2"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAlternateRarities3(self):
        name = "Celestia, Lightsworn Angel"
        version = 2
        rarity = "Ultimate Rare"
        expansion = "LODT"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Light-of-Destruction/Celestia-Lightsworn-Angel-V-2-Ultimate-Rare"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testAlternateRarities4(self):
        name = "Lightning Storm"
        version = 2
        rarity = "Prismatic Secret Rare"
        expansion = "IGAS"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Ignition-Assault/Lightning-Storm-V-2-Prismatic-Secret-Rare"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError1(self):
        name = "Bujintei Tsukuyomi"
        version = 1
        rarity = "Ultra Rare"
        expansion = "LVAL"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Legacy-of-the-Valiant/Bujintei-Tsukuyomi-V-1"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError2(self):
        name = "Divine Dragon Knight Felgrand"
        version = 0
        rarity = "Secret Rare"
        expansion = "MP14"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/2014-MegaTins-MegaPack/Divine-Dragon-Knight-Felgrand"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError3(self):
        name = "Shark Fortress"
        version = 0
        rarity = "Common"
        expansion = "LTGY"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Lord-of-the-Tachyon-Galaxy/Shark-Fortress"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError4(self):
        name = "Meliae of the Trees"
        version = 0
        rarity = "Secret Rare"
        expansion = "MP14"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/2014-MegaTins-MegaPack/Meliae-of-the-Trees"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError5(self):
        name = "Number 39: Utopia"
        version = 1
        rarity = "Ultra Rare"
        expansion = "YS11"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Starter-Deck-Dawn-of-the-Xyz/Number-39-Utopia-V-1-Ultra-Rare"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError6(self):
        name = "Number 96: Dark Mist"
        version = 1
        rarity = "Common"
        expansion = "SP13"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Star-Pack-2013/Number-96-Dark-Mist-V-1-Common"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError7(self):
        name = "Jinzo"
        version = 1
        rarity = "Rare"
        expansion = "BP01"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Battle-Pack-Epic-Dawn/Jinzo-V-1"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError8(self):
        name = "Psi-Blocker"
        version = 1
        rarity = "Common"
        expansion = "BP01"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Battle-Pack-Epic-Dawn/Psi-Blocker-V-1"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


    def testError9(self):
        name = "Typhoon"
        version = 1
        rarity = "Common"
        expansion = "BP03"
        expected = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/Battle-Pack-3-Monster-League/Typhoon-V-1"
        expected += self.modifiers

        returnedURLs = buildURLs(Card(name, version, rarity, expansion, self.condition, self.language, self.firstEd, self.amount, self.price), self.logfile)
        self.assertTrue(expected in returnedURLs, self.getFailureString(expected, returnedURLs))


if __name__ == "__main__":
    unittest.main()