from TaxRate import tax_rates
from app import App
import sys


def help_menu():
    print("Help Menu")
    print('-------------')
    print('-h', "\t", 'afficher ce menu')
    print('\n')
    print('Tax Rates')
    print('-------------')
    for key in tax_rates:
        print(key + "\t" + str(tax_rates[key]))


for arg in sys.argv:
    if arg == "-h":
        help_menu()
        exit(0)

App.run()
