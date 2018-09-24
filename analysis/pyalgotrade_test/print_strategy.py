from pyalgotrade import strategy
from pyalgotrade.barfeed import quandlfeed
from pyalgotrade.barfeed import csvfeed
from pyalgotrade.bar import Frequency


class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(MyStrategy, self).__init__(feed)
        self.__instrument = instrument

    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info(bar.getClose())


# Load the bar feed from the CSV file
feed = csvfeed.GenericBarFeed(Frequency.MINUTE)
# feed.addBarsFromCSV("orcl", "WIKI-ORCL-2000-quandl.csv")
# feed.addBarsFromCSV("orcl", "../../data/input/EURUSD-2018_04_01-2018_09_24.csv")
feed.addBarsFromCSV("orcl", "../../data/input/EURUSD_Candlestick_15_M_ASK_01.04.2018-21.09.2018_after.csv")
# feed.addBarsFromCSV("orcl", "../../data/input/EURUSD-2018_09_23-2018_09_24.csv")
# feed.addBarsFromCSV("orcl", "../../data/input/EURUSD_Candlestick_15_M_BID_01.04.2018-21.09.2018.csv")
# Evaluate the strategy with the feed's bars.
myStrategy = MyStrategy(feed, "orcl")
myStrategy.run()
