class GatewayApilayerGetLastQuotes:
    
    def __init__(self):
        #example: "https://api.apilayer.com/exchangerates_data/latest?symbols=EUR%2CJPY%2CCHF&base=USD"
        self.url = "https://api.apilayer.com/exchangerates_data/latest?symbols=EUR%2CJPY%2CCHF&base=USD"
        
        self.quoteDivider = '%2C'

    def main(self, baseCurrencyAbbr, quoteCurrenciesAbbr):
        




        return {
            'CAD': 2.18,
            'AUD': 2.89,
            'KRW': 1002.01,
            'JPY': 131.84,
            'CHF': 0.92
        }