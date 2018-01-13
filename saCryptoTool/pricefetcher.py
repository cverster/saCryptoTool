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