from adapter.controllerTerminal import ControllerTerminal

test_1 = ControllerTerminal().main()

"""
print("everything is NY NY")
for item in ConvertGivenCurrencies({'USD': 10, 'FAKE_BASE': 100}, ['JPY', 'KRW', 'FAKE_QUOTE', 'CHF', 'INR', '', 'GBP']).main():
    print(item)
"""


print('test completed')




"""
base_usd = BaseCurrency('United States Dollar', 'USD', 100)
base_euro = BaseCurrency('Euro', 'EUR', 10)
base_chf = BaseCurrency('Swiss Frank', 'CHF', 1000)

quote_jpy = QuoteCurrency('JPY', 'Japanese Yen', {'USD': 16, 'EUR': 17, 'CHF': 18})
quote_chy = QuoteCurrency('CHY', 'Chinese Yuan', {'USD': 6, 'EUR': 6.5, 'CHF': 6.9})
quote_chn = QuoteCurrency('CNH', 'Chinese Yuan Offshore', {'USD': 6.2, 'CHF': 7.1})
quote_krw = QuoteCurrency('KRW', 'Korean Won', {'USD': 1308.7})
"""
