# IMPORTS
from binance.client import Client
from forex_python.converter import CurrencyRates

# DECLARATIONS
client = Client("RBYYp91xXqRTslFTns8WUrmEzlx1c14b8vw38AT8Fv0BxsS5IwBa0qNcFDCjxMYm", "9fdncG2T6vVSY4dIJhklupaEsWAgoawrJjNUXrZK1CJHUnbeJt4ohIfLhtPp6vyA")
cRates = CurrencyRates()

# Get non-crypto currencies
usdRates = cRates.get_rates('USD')
zarusd = usdRates["ZAR"]

# get crypto ticker prices
def getPrices():
	prices = client.get_all_tickers()

	#dictionary for zar prices
	pricesZar = {}

	#ethzar
	ethusdt = (item for item in prices if item["symbol"] == "ETHUSDT").next()
	ethzar = float(ethusdt["price"]) * zarusd
	pricesZar['ethzar'] = ethzar

	#btczar
	btcusdt = (item for item in prices if item["symbol"] == "BTCUSDT").next()
	btczar = float(btcusdt["price"]) * zarusd
	pricesZar['btczar'] = btczar

	#venzar
	veneth = (item for item in prices if item["symbol"] == "VENETH").next()
	venusdt = float(veneth["price"]) * float(ethusdt["price"])
	venzar = venusdt * zarusd
	pricesZar['venzar'] = venzar

	#neozar
	neoeth = (item for item in prices if item["symbol"] == "NEOETH").next()
	neousdt = float(neoeth["price"]) * float(ethusdt["price"])
	neozar = neousdt * zarusd
	pricesZar['neozar'] = neozar

	#neblzar
	nebleth = (item for item in prices if item["symbol"] == "NEBLETH").next()
	neblusdt = float(nebleth["price"]) * float(ethusdt["price"])
	neblzar = neblusdt * zarusd
	pricesZar['neblzar'] = neblzar

	#adazar
	adaeth = (item for item in prices if item["symbol"] == "ADAETH").next()
	adausdt = float(adaeth["price"]) * float(ethusdt["price"])
	adazar = adausdt * zarusd 
	pricesZar['adazar'] = adazar

	return pricesZar

def printPrices(pricesZar):
	for item in pricesZar:
		print "%s: R%s" % (item, pricesZar[item])
		#print "%s: R%s" % item.key item 