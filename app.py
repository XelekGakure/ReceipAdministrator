from Item import Item
from Item.Choux import Choux
from Item.Couches import Couches
from List import List


def log(title: str, *items: any):
    print(title)
    print('-------------')
    for i in items:
        print(str(i))
    print('\n')


class App:
    @staticmethod
    def run() -> None:
        print("Hello World")
        my_list = List('CA')

        my_list.add([Choux(), Couches()])

        log("Total Item in List", my_list.number_of_item())
        log("Price Per Item", my_list.price_per_item())
        log("HT Price", my_list.ht_price())
        log("Get Tax Code", my_list.tax_code())
        log("Get Tax Rate", my_list.tax_rate())
        log("TTC Price", my_list.net_price())





