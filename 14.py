class Human:
    def __init__(self, name, age, health):
        self._name = name
        self._age = age
        self._health = health

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value

    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("health cannot be nagative")
        self._health = value

human = Human('Daniil', 24, 100)
print(human.name, human.age, human.health)