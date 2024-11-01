class Character:
    def __init__(self, name, age, race, health):
        self.name = name
        self.age = age
        self.race = race
        self.health = health

    def __str__(self):
        return f"{self.race}, {self.name}, {self.age} лет"

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} получает {damage} урона!. У него осталось {self.health}")
        elif self.health <=0:
            print(f"{self.name}, был убит")

    def buff(self, healing):
        self.health += healing
        print(f"У {self.name} увеличины очки здоровья на {healing}. Теперь у него {self.health} очков здоровья")

    def stealing(self, steal):
        self.health += steal
        print(f"У {self.name} своровали {steal} очков здоровья. Теперь у него {self.health} очков здоровья")


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

    def attack_smbd(self, target):
        print(f"{self.name} атакует {target.name}")
        target.take_damage(self.mana)

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

    def attack_smbd(self, target):
        print(f"{self.name} атакует {target.name}")
        target.take_damage(self.strength)

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

    def attack_smbd(self, target):
        print(f"{self.name} атакует {target.name}")
        target.take_damage(self.accuracy)

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

class Monster(Character):
    def __init__(self, name, age, race, health, stealing_hp):
        super().__init__(name, age, race, health)
        self.stealing_hp = stealing_hp

    def scream(self):
            self. stealing_hp-= self.stealing_hp
            if self.stealing_hp< 0:
                self.stealing_hp += self.stealing_hp
                return "недостаточно очков крика"
            else:
                return f"{self.name} своровал {self.stealing_hp} очков здоровья"

    def steal_hp_smbd(self, target):
        self.health += 50
        print(f"{self.name} своровал здоровье у {target.name}")
        print(f"У {self.name} {self.health} очков здоровья")
        target.stealing(self.stealing_hp)



mage = Mage("Руслан", 14, "Человек", health=200, mana=100)
warrior = Warrior("Богдан", 1, "Орк", health=1000, strength=150)
archer = Archer("Даниил", 25, "Эльф", health=250, accuracy=500)
monk = Monk("Эльдар", 180, "Тёмный эльф", health=500, spiritual_power=400)
monster = Monster("Shadow Fiend", 50, "космодесант", health=5000, stealing_hp=50)

mage.attack_smbd(warrior)
monk.buff_smbd(mage)
monster.steal_hp_smbd(warrior)

