from businessRule.converter import Converter
from adapter.gatewayApilayerGetPossibleCurrenciesAbbrNames import GatewayApilayerGetPossibleCurrenciesAbbrNames


class ConvertGivenCurrencies:
    baseCurrencyAbbr = 'baseCurrencyAbbr'
    baseCurrencyName = 'baseCurrencyName'
    baseCurrencyAmount = 'baseCurrencyAmount'
    quoteCurrencyAbbr = 'quoteCurrencyAbbr'
    quoteCurrencyName = 'quoteCurrencyName'
    quoteCurrencyAmount = 'quoteCurrencyAmount'


    def __init__(self, baseCurrenciesAbbrWithAmount, quoteCurrenciesAbbr):
#{'USD': 100, 'EUR': 100, 'CHF': 100}
        self.baseCurrenciesAbbrWithAmount = baseCurrenciesAbbrWithAmount

#['JPY', 'CHY', 'CHN', 'KRW']
        self.quoteCurrenciesAbbr = quoteCurrenciesAbbr

        self.possibleCurrenciesAbbrNames = GatewayApilayerGetPossibleCurrenciesAbbrNames().main()

        self.gatewayApilayerGetPossibleCurrenciesAbbrNames = GatewayApilayerGetPossibleCurrenciesAbbrNames()

        self.converter = Converter()


    def main(self):
#return: [(False, 'There is no such abbrOfCurrency on our foreigh exchange market'),
#(True, "For 100 United States Dollar(USD) you would get 131.84 Japanese Yen(JPY)"),
# ...,
# {}]     
        existBaseCurrenciesAbbrWithAmount, absentBaseCurrenciesAbbr = self.checkBaseCurrencyExists(self.baseCurrenciesAbbrWithAmount, self.possibleCurrenciesAbbrNames)
        
        existQuoteCurrenciesAbbr, absentQuoteCurrenciesAbbr = self.checkQuoteCurrencyExists(self.quoteCurrenciesAbbr, self.possibleCurrenciesAbbrNames)

        absentCurrenciesResponse = []
        if len(absentBaseCurrenciesAbbr + absentQuoteCurrenciesAbbr) > 0:
            absentCurrenciesResponse = self.getAbsentCurrenciesResponse(absentBaseCurrenciesAbbr + absentQuoteCurrenciesAbbr)

        convertedCurrenciesData = self.getConvetredCurrenciesData(
            existBaseCurrenciesAbbrWithAmount,
            existQuoteCurrenciesAbbr,
            self.gatewayApilayerGetPossibleCurrenciesAbbrNames,
            self.converter
        )

        convertedCurrenciesResponse = self.getConvertedCurrenciesResponse(convertedCurrenciesData, self.possibleCurrenciesAbbrNames)
        
        return convertedCurrenciesResponse + absentCurrenciesResponse


    def checkBaseCurrencyExists(self, baseCurrenciesAbbrWithAmount, possibleCurrenciesAbbrNames):
        existBaseCurrenciesAbbrWithAmount = {}
        absentBaseCurrenciesAbbr = []
        
        for currencyAbbr in baseCurrenciesAbbrWithAmount.keys():
            if currencyAbbr in possibleCurrenciesAbbrNames:
                existBaseCurrenciesAbbrWithAmount[currencyAbbr] = baseCurrenciesAbbrWithAmount[currencyAbbr]
            else:
                absentBaseCurrenciesAbbr.append(currencyAbbr)
        

    def checkQuoteCurrencyExists(self, quoteCurrenciesAbbr, possibleCurrenciesAbbrNames):
        existQuoteCurrenciesAbbr = []
        absentQuoteCurrenciesAbbr = []

        for currencyAbbr in quoteCurrenciesAbbr:
            if currencyAbbr in possibleCurrenciesAbbrNames:
                existQuoteCurrenciesAbbr.append(currencyAbbr)
            else:
                absentQuoteCurrenciesAbbr.append(currencyAbbr)

    def getAbsentCurrenciesResponse(self, absentCurrenciesAbbr):
        absentCurrenciesResponse = []
        for currencyAbbr in absentCurrenciesAbbr:
            absentCurrenciesResponse.append(
                (False, f"There is no such {currencyAbbr} on our foreigh exchange market")
            )
        return absentCurrenciesResponse


    def getConvetredCurrenciesData(self, existBaseCurrenciesAbbrWithAmount, existQuoteCurrenciesAbbr, gatewayApilayerGetPossibleCurrenciesAbbrNames, converter):
#return [{'USD':100, 'CAD': 138}, ..., {})]        
        convertedCurrenciesData = []
        
        for baseCurrency in existBaseCurrenciesAbbrWithAmount.keys():
            baseAmount = existBaseCurrenciesAbbrWithAmount[baseCurrency]
            quotes =  gatewayApilayerGetPossibleCurrenciesAbbrNames(baseCurrency, existQuoteCurrenciesAbbr)   
            for quoteAbbr in quotes.keys():
                quoteRatio = quotes[quoteAbbr]
                convertedCurrenciesData.append({baseCurrency: baseAmount, quoteAbbr: converter.main(baseAmount, quoteRatio)})

        return convertedCurrenciesData


    def getConvertedCurrenciesResponse(self, convertedCurrenciesData, possibleCurrenciesAbbrNames):
#return [(True, "For 100 United States Dollar(USD) you would get 131.84 Japanese Yen(JPY)")]
        response = []

        for currencyData in convertedCurrenciesData:
            baseCurrencyAbbr = currencyData.keys[0]
            baseCurrencyAmount = currencyData.values[0]
            baseCurrencyName = possibleCurrenciesAbbrNames[baseCurrencyAbbr]
            quoteCurrencyAbbr = currencyData.keys[1]
            quoteCurrencyAmount = currencyData.values[1]
            quoteCurrencyName = possibleCurrenciesAbbrNames[quoteCurrencyAbbr]
            response.append(
                True,
                f"For {baseCurrencyAmount} {baseCurrencyName}({baseCurrencyAbbr}) you would get {quoteCurrencyAmount} {quoteCurrencyName}({quoteCurrencyAbbr}})"
            )


 