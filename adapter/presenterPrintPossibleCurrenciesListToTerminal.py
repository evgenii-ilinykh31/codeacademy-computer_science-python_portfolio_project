class PresenterPrintPossibleCurrenciesListToTerminal:

    def main(self, possibleCurrenciesAbbrNames):
    #{
    #   'USD': 'UNITED STATES DOLLAR',
    #   'AUD': 'AUSTRALIAN DOLLAR',
    #   'CAD': 'CANADIAN DOLLAR',
    #   'EUR': 'EURO',
    #   'JPY': 'JAPANESE YEN',
    #   'CHF': 'SWISS FRANK',
    #   'KRW': 'KOREAN WON'
    #}
        print('List of all currencies for which we could provide exchange rates:')
        for abbr, name in possibleCurrenciesAbbrNames.items():
            print(f"{abbr}: {name}")