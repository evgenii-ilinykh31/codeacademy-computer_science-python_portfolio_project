import requests
import sys
import json
from interface.interfaceWebApilayer import InterfaceWebApilayer

class GatewayApilayerGetLastQuotes:
    
    def __init__(self):        
        self.quoteDelimiter = '%2C'
        self.payload = {}
        self.headers = {"apikey": "iT5FfwzzrqCaatDrP6qnRAJtRRIEe9Mz"}
        self.rates = 'rates'
        self.interfaceWebApilayer = InterfaceWebApilayer()


    def main(self, baseCurrencyAbbr, quoteCurrenciesAbbrs):
    #"USD"
    #["CAD", "JPY", "CHF"]
    #return {
    #     'CAD': 2.18,
    #     'AUD': 2.89,
    #     'KRW': 1002.01,
    #     'JPY': 131.84,
    #     'CHF': 0.92
    #}    
        requestUrl = self.getUrl(baseCurrencyAbbr, quoteCurrenciesAbbrs, self.quoteDelimiter)

        responseParse = self.interfaceWebApilayer.main(requestUrl, self.payload, self.headers)

        return responseParse[self.rates]
    

    def getUrl(self, baseCurrencyAbbr, quoteCurrenciesAbbrs, quoteDelimiter):
    #"USD"
    #["CAD", "JPY", "CHF"]     
    #return: "https://api.apilayer.com/exchangerates_data/latest?symbols=EUR%2CJPY%2CCHF&base=USD"
        quoteCurrenciesAbbrsString = ''.join([abbr+quoteDelimiter for abbr in quoteCurrenciesAbbrs])[:-len(quoteDelimiter)]
        return f"https://api.apilayer.com/exchangerates_data/latest?symbols={quoteCurrenciesAbbrsString}&base={baseCurrencyAbbr}"