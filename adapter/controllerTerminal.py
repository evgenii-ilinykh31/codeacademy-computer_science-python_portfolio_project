from usecase.convertGivenCurrencies import ConvertGivenCurrencies
from usecase.getPossibleCurrenciesAbbrNames import GetPossibleCurrenciesAbbrNames
import re


class ControllerTerminal:
    
    def __init__(self):
        self.codes = 'codes'
        self.pattern = "^\s*([a-zA-Z]{3}\s*:\s*\d+\s*,\s*)*([a-zA-Z]{3}\s*:\s*\d+){1}\s*-\s*([a-zA-Z]{3}\s*,\s*)*([a-zA-Z]{3}){1}\s*$"
        self.greetings = f"""
Greetings! Thank you for using of our service!

If you want to get last currency rates - please  message in format below and hit enter. You can use spaces - they would be ignored:
    XXX:z1,YYY:z2-AAA,BBB,CCC
    where XXX, YYY - base currencies ISO 4217 codes
    z1, z2 - amounts which you want to calculate
    AAA,BBB,CCC - quoted currencies ISO 4217 codes

If you want to see available currency codes - please type word "{self.codes}" and hit enter.          

Please type: """


    def main(self):
        answer = ''
        while not self.checkInput(answer, [self.codes], [self.pattern]):
            answer = self.doGreetingsGetInput(self.greetings)
        if answer == self.codes:
            GetPossibleCurrenciesAbbrNames().main()
        else:
            baseCurrenciesAbbrWithAmount, quoteCurrenciesAbbr = self.deassambleGetQuotesAnswerToBaseAndQuotesCurrencies(answer)
            
            #ConvertGivenCurrencies(baseCurrenciesAbbrWithAmount, quoteCurrenciesAbbr).main()


    def checkInput(self, answer = '', checkWords = [], checkPatternsForRe = []):
        for word in checkWords:
            if answer == word:
                return True
        for pattern in checkPatternsForRe:
            if re.compile(pattern).match(answer):
                return True


    def doGreetingsGetInput(self, greetings):
        return input(greetings)
    

    def deassambleGetQuotesAnswerToBaseAndQuotesCurrencies(self, answer):
        answer = answer.replace(" ", "").split('-')

        baseCurrenciesAbbrWithAmount = []
        for abbrAmountPair in answer[0].split(','):
            abbrAmountPair = abbrAmountPair.split(':')
            baseCurrenciesAbbrWithAmount.append({abbrAmountPair[0]:abbrAmountPair[1]})
        
        quoteCurrenciesAbbr = answer[1].split(',')

        return baseCurrenciesAbbrWithAmount, quoteCurrenciesAbbr
    
    