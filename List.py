from Item import Item
from TaxRate import tax_rates


class List:
    __items: [Item] = []
    __tax_code: str

    def __init__(self, tax_code: str) -> None:
        self.__tax_code = tax_code

    def add(self, items: [Item]) -> None:
        for item in items:
            self.__items.append(item)

    def price_per_item(self) -> [float]:
        prices = []
        for item in self.__items:
            prices.append(item.price())
        return prices

    def number_of_item(self):
        return len(self.__items)

    def ht_price(self) -> float:
        price = 0
        for item in self.__items:
            price += item.price()
        return price

    def tax_code(self) -> str:
        return self.__tax_code

    def tax_rate(self) -> float:
        return tax_rates.get(self.__tax_code)

    def net_price(self) -> float:
        return self.ht_price() + (self.ht_price() * self.tax_rate() / 100)
