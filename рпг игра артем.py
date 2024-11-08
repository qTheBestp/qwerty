class Character:
    def __init__(self, name, age, race, health):
        self.name = name
        self.age = age
        self.race = race
        self.health = health
        self.items = []

    def __str__(self):
        return f"{self.race}, {self.name}, {self.age} лет"

    def health_down(self, damage, name_monster):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} получает {damage} урона от {name_monster}!. У него осталось {self.health}")
        elif self.health <=0:
            print(f"{self.name}, был убит от рук {name_monster}")

    def buff(self, healing):
        self.health += healing
        print(f"У {self.name} увеличины очки здоровья на {healing}. Теперь у него {self.health} очков здоровья")

    def stealing(self, steal):
        self.health -= steal
        print(f"У {self.name} своровали {steal} очков здоровья. Теперь у него {self.health} очков здоровья")

    def get_health(self):
        print(f"У {self.name} осталось {self.health} очков здоровья")

    def health_up(self, num):
        self.health += num.health
        print(f"Здоровье повышено на {num.health} единиц")

    def find(self, item):
        self.items.append(item)
        print(f"{self.name} поднял {item}")

    def throw(self, item):
        self.items.remove(item)
        print(f"{self.name} выбросил {item}")



class Mage(Character):
    def __init__(self, name, age, race, health, mana):
        super().__init__(name, age, race, health)
        self.mana = mana

    def cast_spell(self):
        self.mana -= self.mana
        if self.mana < 0:
            self.mana += self.mana
            return "недостаточно очков маны"
        else:
            return f"{self.name} использовал магию, стоимостью {self.mana} очков маны"



    def get_mana(self):
        print(f"У {self.name} осталось {self.mana} очков маны")

    def take_damage(self, target):
        print(f"{self.name} атакует с силой {self.mana}!")
        target.health_down(self.mana, self.name)

class Warrior(Character):
    def __init__(self, name, age, race, health, strength):
        super().__init__(name, age, race, health)
        self.strength = strength

    def attack(self):
        self.strength -= self.strength
        if self.strength < 0:
            self.strength += self.strength
            return "недостаточно очков силы"
        else:
            return f"{self.name} сделал мощный удар, использовав {self.strength} очков силы"

    def get_strength(self):
        print(f"У {self.name} осталось {self.strength} очков силы")


    def take_damage(self, target):
        print(f"{self.name} атакует с силой {self.strength}!")
        target.health_down(self.strength, self.name)


class Archer(Character):
    def __init__(self, name, age, race, health, accuracy):
        super().__init__(name, age, race, health)
        self.accuracy = accuracy

    def shoot_arrow(self):
            self.accuracy -= self.accuracy
            if self.accuracy < 0:
                self.accuracy += self.accuracy
                return "недостаточно очков меткости"
            else:
                return f"{self.name} сделал точный выстрел, использовав {self.accuracy} очков меткости"


    def get_accuracy(self):
        print(f"У {self.name} осталось {self.accuracy} очков меткости")

    def take_damage(self, target):
        print(f"{self.name} атакует с силой {self.accuracy}!")
        target.health_down(self.accuracy, self.name)

class Monk(Character):
    def __init__(self, name, age, race, health, spiritual_power):
        super().__init__(name, age, race, health)
        self.spiritual_power = spiritual_power

    def meditate(self):
        self.spiritual_power -= self.spiritual_power
        if self.spiritual_power < 0:
            self.spiritual_power += self.spiritual_power
            return "недостаточно очков духовной силы"
        else:
            self.health += 150
            return f"{self.name} увеличивает очки здоровья союзника на 150, используя {self.spiritual_power} очков духовной силы"

    def buff_smbd(self, target):
        print(f"{self.name} увеличивает очки здоровья {target.name}")
        target.buff(self.spiritual_power)

    def get_spiritual_power(self):
        print(f"У {self.name} осталось {self.spiritual_power} очков духовной силы")

    def take_damage(self, target):
            print(f"{self.name} атакует с силой {self.spiritual_power}!")
            target.health_down(self.spiritual_power, self.name)


class Monster(Character):
    def __init__(self, name, age, race, health, stealing_hp):
        super().__init__(name, age, race, health)
        self.stealing_hp = stealing_hp

    def scream(self):
            self.stealing_hp -= self.stealing_hp
            if self.stealing_hp< 0:
                self.stealing_hp += self.stealing_hp
                return "недостаточно очков воровства"
            else:
                return f"{self.name} своровал {self.stealing_hp} очков здоровья"

    def steal_hp_smbd(self, target):
        self.health += 50
        print(f"{self.name} своровал здоровье у {target.name}")
        print(f"У {self.name} {self.health} очков здоровья")
        target.stealing(self.stealing_hp)

    def get_stealing_hp(self):
        print(f"У {self.name} осталось {self.health} очков воровства")

    def take_damage(self, target):
            print(f"{self.name} атакует с силой {self.stealing_hp}!")
            target.health_down(self.stealing_hp, self.name)



class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, target):
        print(f"{target.name} использует {self.name}")
        print(f"{target.name} восстановливает {self.effect} здоровья!")
        target.health_up(self.effect)

class Food(Item):
    def __init__(self, name, health_value):
        super().__init__(name)
        self.health_value = health_value

    def eat(self, target):
        target.health_up(self.health_value)



mage = Mage("Руслан", 14, "Человек", health=200, mana=200)
warrior = Warrior("Богдан", 1, "Орк", health=1000, strength=150)
archer = Archer("Даниил", 25, "Эльф", health=250, accuracy=500)
monk = Monk("Эльдар", 180, "Тёмный эльф", health=500, spiritual_power=400)
monster = Monster("Shadow Fiend", 50, "космодесант", health=2000, stealing_hp=100)


monk.buff_smbd(mage)
monster.steal_hp_smbd(warrior)
archer.take_damage(monster)

t1 = Item("Яблоко", 10)
monk.find(t1)
t1.use(monk)