import random
import time

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
            print(f"{self.name} получает {damage} урона от {name_monster}!. У него осталось {self.health} здоровья")
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
        self.health += num
        print(f"Здоровье повышено на {num} единиц")

    def health_daun(self, num):
        self.health -= num
        print(f"Здоровье понижено на {num}")

    def find(self, item):
        self.items.append(item)
        print(f"{self.name} поднял {item.name}")

    def throw(self, item):
        self.items.remove(item)
        print(f"{self.name} выбросил {item.name}")





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

    def mana_up(self, num):
        self.mana += num
        print(f"Мана повысилась на {num}, теперь у {self.name} {self.mana} очков маны")

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

    def strength_up(self, num):
        self.strength += num
        print(f"Сила повысилась на {num}, теперь у {self.name} {self.strength} очков силы")

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

    def accuracy_up(self, num):
        self.accuracy += num
        print(f"Меткость повысилась на {num}, теперь у {self.name} {self.accuracy} очков меткости")

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

    def spiritual_power_up(self, num):
        self.spiritual_power += num
        print(f"Духовная сила повысилась на {num}, теперь у {self.name} {self.spiritual_power} очков духовной силы")

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
            if self.stealing_hp < 0:
                self.stealing_hp += self.stealing_hp
                return "недостаточно очков воровства"
            else:
                return f"{self.name} своровал {self.stealing_hp} очков здоровья"

    def stealing_hp_up(self, num):
        self.stealing_hp += num
        print(f"Воровство повысилась на {num}, теперь у {self.name} {self.stealing_hp} очков воровства")

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

    def get_info(self):
        if self.effect > 0:
            print(f"{self.name} обладает эффектом восстановления здоровья на {self.effect} единиц")
        else:
            print(f"{self.name} обладает эффектом понижения здоровья на {self.effect} единиц")


class Food(Item):
    def __init__(self, name):
        self.name = name
        self.effect = random.randint(-10, 110)

    def get_heal(self, user):
        if self.effect < 0:
            print(f"{self.name} отравило {user.name}")
            user.health_daun(abs(self.effect))
        else:
            print(f"{self.name} восстанавливает здоровье {user.name}")
            user.health_up(self.effect)

class Weapons(Item):
    def __init__(self, name):
        self.name = name
        self.effect = random.randint(10, 110)

    def damage_up(self, user):
        print(f"{self.name} увеличил урон {user.name} на {self.effect}")
        if user == Mage:
            user.mana_up(self.effect)
        elif user == Warrior:
            user.strength_up(self.effect)
        elif user == Archer:
            user.accuracy_up(self.effect)
        elif user == Monk:
            user.spiritual_power_up(self.effect)
        elif user == Monster:
            user.stealing_hp(self.effect)





mage = Mage("Руслан", 14, "Человек", health=200, mana=200)
warrior = Warrior("Богдан", 1, "Орк", health=1000, strength=150)
archer = Archer("Даниил", 25, "Эльф", health=250, accuracy=500)
monk = Monk("Эльдар", 180, "Тёмный эльф", health=500, spiritual_power=400)
monster = Monster("Shadow Fiend", 50, "Космодесант", health=2000, stealing_hp=100)


monk.buff_smbd(mage)
time.sleep(5)
monster.steal_hp_smbd(warrior)
time.sleep(5)
archer.take_damage(monster)
time.sleep(5)
t2 = Weapons("Daedalus")
t1 = Food("Яблоко")
monk.find(t1)
time.sleep(5)
monk.find(t2)
time.sleep(3)
t1.get_heal(monk)
time.sleep(3)
t2.damage_up(monk)

