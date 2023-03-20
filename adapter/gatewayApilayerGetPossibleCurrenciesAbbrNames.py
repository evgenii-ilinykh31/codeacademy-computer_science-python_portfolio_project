from interface.interfaceWebApilayer import InterfaceWebApilayer


class GatewayApilayerGetPossibleCurrenciesAbbrNames:

    def __init__(self):
        self.url = "https://api.apilayer.com/exchangerates_data/symbols"
        self.payload = {}
        self.headers = {"apikey": "iT5FfwzzrqCaatDrP6qnRAJtRRIEe9Mz"}
        self.interfaceWebApilayer = InterfaceWebApilayer()
        self.symbols = 'symbols'


    def main(self):
        responseParse = self.interfaceWebApilayer.main(self.url, self.payload, self.headers)
        return responseParse[self.symbols]
        #return {
        #   'USD': 'UNITED STATES DOLLAR',
        #   'AUD': 'AUSTRALIAN DOLLAR',
        #   'CAD': 'CANADIAN DOLLAR',
        #   'EUR': 'EURO',
        #   'JPY': 'JAPANESE YEN',
        #   'CHF': 'SWISS FRANK',
        #   'KRW': 'KOREAN WON'
        #}             