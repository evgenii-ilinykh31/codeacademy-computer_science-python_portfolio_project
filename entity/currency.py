class Currency:

    def __init__(self, name, abbr, ratios = {}):
        self.name = name
        self.abbr = abbr
#ratios should be like that: {currencyAbbr: ratioToThisCurrency}        
        self.ratios = ratios
        self.noRatioMessage = 'no ratio'

    def getName(self):
        return self.name
    
    def getAbbr(self):
        return self.name
    
    def getRatio(self, currencyAbbr):
        if currencyAbbr in self.ratios:
            return self.ratios[currencyAbbr]
        else:
            return self.noRatioMessage 
