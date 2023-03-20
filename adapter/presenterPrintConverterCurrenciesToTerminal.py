from interface.interfaceTerminal import InterfaceTerminal


class PresenterPrintConverterCurrenciesToTerminal:

    def __init__(self):
        self.interfaceTerminal = InterfaceTerminal()
    

    def main(self, listOfConvertedCurrenciesResponses):
    #[(False, 'There is no such abbrOfCurrency on our foreigh exchange market'),
    #(True, "For 100 United States Dollar(USD) you would get 131.84 Japanese Yen(JPY)"),
    # ...,
    # {}]
        messages = []
        
        for response in listOfConvertedCurrenciesResponses:
            message = ''
            if response[0]:
                message += 'Success: '
            else:
                message += 'Error: '
            message += response[1]
            messages.append(message)
        
        self.interfaceTerminal.main(messages)