# IMPORTS
from binance.client import Client
from forex_python.converter import CurrencyRates

# DECLARATIONS
api_key = ""
api_secret = ""
client = Client(api_key, api_secret)
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

	#iotazar
	iotaeth = (item for item in prices if item["symbol"] == "IOTAETH").next()
	iotausdt = float(iotaeth["price"]) * float(ethusdt["price"])
	iotazar = iotausdt * zarusd
	pricesZar['iotazar'] = iotazar

	#arnzar
	arneth = (item for item in prices if item["symbol"] == "ARNETH").next()
	arnusdt = float(arneth["price"]) * float(ethusdt["price"])
	arnzar = arnusdt * zarusd
	pricesZar['arnzar'] = arnzar

	#xrpzar
	xrpeth = (item for item in prices if item["symbol"] == "XRPETH").next()
	xrpusdt = float(xrpeth["price"]) * float(ethusdt["price"])
	xrpzar = xrpusdt * zarusd
	pricesZar['xrpzar'] = xrpzar

	#trxzar
	trxeth = (item for item in prices if item["symbol"] == "XRPETH").next()
	trxusdt = float(trxeth["price"]) * float(ethusdt["price"])
	trxzar = trxusdt * zarusd
	pricesZar['trxzar'] = trxzar

	#cmtzar
	cmteth = (item for item in prices if item["symbol"] == "CMTETH").next()
	cmtusdt = float(cmteth["price"]) * float(ethusdt["price"])
	cmtzar = cmtusdt * zarusd
	pricesZar['cmtzar'] = cmtzar

	return pricesZar

def getValues(userid, prices, db):

	# empty values list
	values = {}

	# with sqlite3
	cursor2 = db.cursor()
	cursor2.execute('SELECT coin, balance FROM currentBalances WHERE userid = :userid', {'userid': userid})
	total = 0

	for coin, balance in cursor2:
		if coin == 'BTC':
			values['Bitcoin'] = float(balance) * float(prices['btczar'])
			total = total + values['Bitcoin']
		elif coin == 'ETH':
			values['Ethereum'] = float(balance) * float(prices['ethzar'])
			total = total + values['Ethereum']
		elif coin == 'NEO':
			values['Neo'] = float(balance) * float(prices['neozar'])
			total = total + values['Neo']
		elif coin == 'ADA':
			values['Cardano'] = float(balance) * float(prices['adazar'])
			total = total + values['Cardano']
		elif coin == 'VEN':
			values['Vechain'] = float(balance) * float(prices['venzar'])
			total = total + values['Vechain']
		elif coin == 'NEBL':
			values['Neblio'] = float(balance) * float(prices['neblzar'])
			total = total + values['Neblio']
		elif coin == 'IOTA':
			values['Iota'] = float(balance) * float(prices['iotazar'])
			total = total + values['Iota']
		elif coin == 'ARN':
			values['Aeron'] = float(balance) * float(prices['arnzar'])
			total = total + values['Aeron']
		elif coin == 'XRP':
			values['Ripple'] = float(balance) * float(prices['xrpzar'])
			total = total + values['Ripple']
		elif coin == 'TRX':
			values['Tron'] = float(balance) * float(prices['trxzar'])
			total = total + values['Tron']
		elif coin == 'CMT':
			values['Comet'] = float(balance) * float(prices['cmtzar'])
			total = total + values['Comet']
		values['Total'] = total

	return values
 	

def printPrices(pricesZar):
	print "Here are the crypto prices in ZAR:"
	print "=================================="
	for item in pricesZar:
		print "%s: R%s" % (item, pricesZar[item])
		#print "%s: R%s" % item.key item 
	print "=================================="