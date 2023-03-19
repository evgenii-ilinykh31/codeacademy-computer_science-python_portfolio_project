from businessRule.converter import Converter
from adapter.gatewayApilayerGetPossibleCurrenciesAbbrNames import GatewayApilayerGetPossibleCurrenciesAbbrNames
from adapter.gatewayApilayerGetLastQuotes import GatewayApilayerGetLastQuotes


class ConvertGivenCurrencies:

    def __init__(self, baseCurrenciesAbbrWithAmount, quoteCurrenciesAbbr):
    #{'USD': 100, 'EUR': 100, 'CHF': 100}
        self.baseCurrenciesAbbrWithAmount = baseCurrenciesAbbrWithAmount
    #['JPY', 'CHY', 'CHN', 'KRW']
        self.quoteCurrenciesAbbr = quoteCurrenciesAbbr

        self.possibleCurrenciesAbbrNames = GatewayApilayerGetPossibleCurrenciesAbbrNames().main()

        self.gatewayApilayerGetLastQuotes = GatewayApilayerGetLastQuotes()

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
 
        convertedCurrenciesData = []

        if len(existBaseCurrenciesAbbrWithAmount) > 0 and len(existQuoteCurrenciesAbbr) > 0:
            convertedCurrenciesData = self.getConvetredCurrenciesData(
                existBaseCurrenciesAbbrWithAmount,
                existQuoteCurrenciesAbbr,
                self.gatewayApilayerGetLastQuotes,
                self.converter
            )
            convertedCurrenciesResponse = self.getConvertedCurrenciesResponse(convertedCurrenciesData, self.possibleCurrenciesAbbrNames)
       
        return absentCurrenciesResponse + convertedCurrenciesResponse


    def checkBaseCurrencyExists(self, baseCurrenciesAbbrWithAmount, possibleCurrenciesAbbrNames):
        existBaseCurrenciesAbbrWithAmount = {}
        absentBaseCurrenciesAbbr = []
        
        for currencyAbbr in baseCurrenciesAbbrWithAmount.keys():
            if currencyAbbr in possibleCurrenciesAbbrNames:
                existBaseCurrenciesAbbrWithAmount[currencyAbbr] = baseCurrenciesAbbrWithAmount[currencyAbbr]
            else:
                absentBaseCurrenciesAbbr.append(currencyAbbr)
       
        return existBaseCurrenciesAbbrWithAmount, absentBaseCurrenciesAbbr


    def checkQuoteCurrencyExists(self, quoteCurrenciesAbbr, possibleCurrenciesAbbrNames):
        existQuoteCurrenciesAbbr = []
        absentQuoteCurrenciesAbbr = []

        for currencyAbbr in quoteCurrenciesAbbr:
            if currencyAbbr in possibleCurrenciesAbbrNames:
                existQuoteCurrenciesAbbr.append(currencyAbbr)
            else:
                absentQuoteCurrenciesAbbr.append(currencyAbbr)
        
        return existQuoteCurrenciesAbbr, absentQuoteCurrenciesAbbr

    def getAbsentCurrenciesResponse(self, absentCurrenciesAbbr):
        absentCurrenciesResponse = []
        for currencyAbbr in absentCurrenciesAbbr:
            absentCurrenciesResponse.append(
                (False, f"There is no such {currencyAbbr} on our foreigh exchange market")
            )
        return absentCurrenciesResponse


    def getConvetredCurrenciesData(self, existBaseCurrenciesAbbrWithAmount, existQuoteCurrenciesAbbrs, gatewayApilayerGetLastQuotes, converter):
    #return [{'USD':100, 'CAD': 138}, ..., {})]        
        convertedCurrenciesData = []
        
        for baseCurrencyAbbr in existBaseCurrenciesAbbrWithAmount.keys():
            baseAmount = existBaseCurrenciesAbbrWithAmount[baseCurrencyAbbr]
            quotes =  gatewayApilayerGetLastQuotes.main(baseCurrencyAbbr, existQuoteCurrenciesAbbrs)   
            for quoteAbbr in quotes.keys():
                quoteRatio = quotes[quoteAbbr]
                convertedCurrenciesData.append({baseCurrencyAbbr: baseAmount, quoteAbbr: converter.main(baseAmount, quoteRatio)})

        return convertedCurrenciesData


    def getConvertedCurrenciesResponse(self, convertedCurrenciesData, possibleCurrenciesAbbrNames):
    #return [(True, "For 100 United States Dollar(USD) you would get 131.84 Japanese Yen(JPY)")]
        response = []
        
        for currencyData in convertedCurrenciesData:
            currencyDataAbbrs = list(currencyData.keys())
            currencyDataAmounts = list(currencyData.values())

            baseCurrencyAbbr = currencyDataAbbrs[0]
            baseCurrencyAmount = currencyDataAmounts[0]
            baseCurrencyName = possibleCurrenciesAbbrNames[baseCurrencyAbbr]

            quoteCurrencyAbbr = currencyDataAbbrs[1]
            quoteCurrencyAmount = currencyDataAmounts[1]
            quoteCurrencyName = possibleCurrenciesAbbrNames[quoteCurrencyAbbr]

            response.append(
                (True,
                f"For {baseCurrencyAmount} {baseCurrencyName}({baseCurrencyAbbr}) you would get {round(quoteCurrencyAmount, 3)} {quoteCurrencyName}({quoteCurrencyAbbr})")
            )

        return response


 