class Item:
    __price: float = 0
    __name: str = "New Item"

    def __init__(self, price: float, name: str = "New Item") -> None:
        self.__price = price
        self.__name = name

    def price(self) -> float:
        return self.__price

    def name(self) -> str:
        return self.__name
