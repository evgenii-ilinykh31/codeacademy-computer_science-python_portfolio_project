from adapter.presenterPrintPossibleCurrenciesListToTerminal import PresenterPrintPossibleCurrenciesListToTerminal
from adapter.gatewayApilayerGetPossibleCurrenciesAbbrNames import GatewayApilayerGetPossibleCurrenciesAbbrNames

class GetPossibleCurrenciesAbbrNames:
    
    def main(self):

        possibleCurrenciesAbbrNames = GatewayApilayerGetPossibleCurrenciesAbbrNames().main()