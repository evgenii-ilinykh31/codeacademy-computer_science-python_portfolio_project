from interface.interfaceTerminal import InterfaceTerminal


class PresenterPrintPossibleCurrenciesListToTerminal:

    def __init__(self):
        self.interfaceTerminal = InterfaceTerminal()


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
        messages = ['List of all currencies for which we could provide exchange rates:']
        for abbr, name in possibleCurrenciesAbbrNames.items():
            messages.append(f"{abbr}: {name}")
        
        self.interfaceTerminal.main(messages)