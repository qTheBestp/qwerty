class Thing:
    def __init__(self, price, durability):
        self._price = price
        self._durability = durability

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

    @property
    def durability(self):
        return self._durability
    @durability.setter
    def durability(self, value):
        if value < 0:
            raise ValueError("durability cannot be negative")
        self._durability = value

string = Thing(10, 5)
print(string.price, string.durability)