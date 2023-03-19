import requests
import sys
import json

class GatewayApilayerGetLastQuotes:
    
    def __init__(self):        
        self.quoteDelimiter = '%2C'
        self.payload = {}
        self.headers = {"apikey": "iT5FfwzzrqCaatDrP6qnRAJtRRIEe9Mz"}


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

        return self.getApilayerResponse(requestUrl, self.payload, self.headers)    
    

    def getUrl(self, baseCurrencyAbbr, quoteCurrenciesAbbrs, quoteDelimiter):
    #"USD"
    #["CAD", "JPY", "CHF"]     
    #return: "https://api.apilayer.com/exchangerates_data/latest?symbols=EUR%2CJPY%2CCHF&base=USD"
        quoteCurrenciesAbbrsString = ''.join([abbr+quoteDelimiter for abbr in quoteCurrenciesAbbrs])[:-len(quoteDelimiter)]
        return f"https://api.apilayer.com/exchangerates_data/latest?symbols={quoteCurrenciesAbbrsString}&base={baseCurrencyAbbr}"
    

    def getApilayerResponse(self, url, payload, headers):
        response = ''
        statusCode = 0
        requestCounter = 0
        while requestCounter < 3 and statusCode != 200:
            response = requests.request("GET", url, headers = headers, data = payload)
            statusCode = response.status_code
        if statusCode != 200:
            sys.exit(f"something wrong with server | statusCode: {statusCode}")
            #todo: add logging of mistake

        responseParse = json.loads(response.text)
        if not responseParse['success']: 
            sys.exit(f"something wrong with server | responseParse: {responseParse}")
            #todo: add logging of mistake           
 
        return responseParse['rates']

        # request on response | string:
        #  {
        #    "base": "USD",
        #    "date": "2023-03-19",
        #    "rates": {
        #      "CHF": 0.922739,
        #      "EUR": 0.93005,
        #      "JPY": 132.394008
        #    },
        #    "success": true,
        #    "timestamp": 1679253603
        #  }