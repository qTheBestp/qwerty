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
        elif self.health <= 0:
            print(f"{self.name}, был убит руками {name_monster}")

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

    def use(self, name_item):
        target = ""
        for item in self.items:
            if item.name == name_item:
                target = item
        if target != "":
            print(f"{self.name} использует {target.name}!")
            target.get_heal(self)
            self.items.remove(target)
        else:
            print(f"{name_item} нету в инвентаре")



class Mage(Character):
    def __init__(self, name, age, race, health, mana):
        super().__init__(name, age, race, health)
        self.mana = mana

    def attack(self, target):
        f"""{self.name} использовал магию, стоимостью {self.mana} очков маны"""
        target.health_down(self.mana, self.name)

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

    def attack(self, target):
        f"""{self.name} сделал мощный удар, использовав {self.strength} очков силы"""
        target.health_down(self.strength, self.name)

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

    def attack(self, target):
        f"""{self.name} сделал точный выстрел, использовав {self.accuracy} очков меткости"""
        target.health_down(self.accuracy, self.name)

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

    def attack(self, target):
        f"""{self.name} увеличивает очки здоровья союзника на 150, используя {self.spiritual_power} очков духовной силы"""
        target.health_down(self.spiritual_power, self.name)


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

    def attack(self, target):
        f"""{self.name} своровал {self.stealing_hp} очков здоровья."""
        target.health_down(self.stealing_hp, self.name)

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

    def get_heal(self, user):
        if self.effect < 0:
            print(f"{self.name} отравило {user.name}")
            user.health_daun(abs(self.effect))
        else:
            print(f"{self.name} восстанавливает здоровье {user.name}")
            user.health_up(self.effect)



class Food(Item):
    def __init__(self, name):
        self.name = name
        self.effect = random.randint(-10, 110)


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


def fight(user, monster):
    while user.health > 0 or monster.health > 0:
        if monster.health > 0:
            monster.attack(user)
        else:
            break
        time.sleep(2)
        if user.health > 0:
            user.attack(monster)
        else:
            break
        if user.health <= 100:
            heal = int(input("У вас мало здоровья, вы хотите испотзовать аптечку? 1 - да, 2 - нет"))
            if heal == 1:
                user.use("малая аптечка") or user.use("средняя аптечка") or user.use("большая аптечка")
                user.get_health()
            elif heal == 2:
                user.get_health()


def Main():
    print("""
    Игрок просыпается в полуразрушенной башне, окруженной густым туманом.
    Память фрагментарна: последнее, что помнит персонаж – это ослепительная вспышка света и оглушительный грохот.
    Он/она находится в лохмотьях, рядом лежит сломанный посох, очевидно, некогда бывший могущественным орудием.
    Внезапно, башню сотрясает землятресение, заставляя персонажа поспешить найти убежище.

    Во время поисков безопасного места, игрок натыкается на полузасыпанную комнату, в которой находит письмо.
    Письмо написано древним шрифтом и рассказывает о “Пророчестве Заката” – легенде о том, что в час величайшей тьмы родится избранный, способный спасти Аэтор.
    В письме также упоминается символ, похожий на татуировку на запястье игрока, который он/она до сих пор не замечал(а).

    Выйдя из башни, игрок оказывается в мрачном лесу, окруженном руинами бывшего великолепного города.
    Он/она встречает умирающего старика, который перед смертью рассказывает о “Ключе к Рассвету” – артефакте, способном вернуть Аэтору былую славу.
    Старик говорит, что путь к нему лежит через “Запретный Храм”, однако предупреждает о опасности, подстерегающей путешественника.
    С этими словами старик умирает, оставляя игрока наедине с суровой реальностью умирающего мира.

    Звуки ветра и скрип старой древесины заполняют тишину. Туман клубится вокруг тебя, скрывая то, что ждет впереди.
    Пробуждение… или, быть может, возрождение?

    Ты чувствуешь прилив странной силы, эхо прошлого, шепчущее тебе на ухо о забытых временах и грядущих битвах.
    Символ на твоем запястье пульсирует, напоминая о предназначении, которое ты пока еще не в силах постичь.
    Аэтор ждет своего спасителя… или, возможно, палача? Выбор за тобой.
    """)
#    time.sleep(60)

    user = ""
    name = input("Введите имя")
    age = int(input("Введите возраст"))
    race = input("Введите расу")
    class_user = int(input("Выберите класс персонажа: 1 - маг, 2 - воин, 3 - лучник, 4 - монах"))
#    time.sleep(3)
    if class_user == 1:
        user = Mage(name, age, race, 100, 75)

        print(f"""
        {name}, маг… Имя, прошептанное ветром сквозь руины. Класс, предначертанный звездами.
        Ты выбрал(а) свой путь, и теперь судьба Аэтора в твоих руках. Темные силы уже чувствуют твое приближение…
        Будь осторожен(а).
        """)
    elif class_user == 2:
        user = Warrior(name, age, race, 250, 50)
        print(f"""
        Здравствуй, {name}, воин! Рад приветствовать тебя в рядах тех, кто стремится спасти Аэтор.
        Как воин, ты обладаешь уникальными навыками и способностями, которые станут тебе верными союзниками в этом нелегком путешествии.
        Помни, путь предстоит долгий и опасный, но вместе мы преодолеем любые трудности!
        """)
    elif class_user == 3:
        user = Archer(name, age, race, 75, 100)
        print(f"""
        {name}, лучник. Ну, чего стоишь? Аэтор ждет. Начинаем!
        """)
    elif class_user == 4:
        user = Monk(name, age, race, 150, 50)
        print(f"""
        Так значит, тебя зовут {name}, монах. Аэтор помнит твои деяния еще до твоего рождения. Пророчество сбывается.
        Твой путь начинается сейчас, {name}, и от твоих решений зависит судьба всего мира.
        Пусть духовная сила монаха будет твоим щитом и мечом в этой борьбе за свет.
        """)
    else:
        print(f"""
        Привет, {name}! Ну что, готов(а) спасти мир? Надеюсь, ты взял(а) с собой запасные штаны, потому что грязи тут будет по колено!
        Давай исправляй то что ты наделал. Такого класса нету!
        """)
        raise ValueError("Вы выбрали несуществующую расу")
#    time.sleep(5)

    print(f"""Получено новое задание: достичь “Запретного Храма” и разобраться с причинами катастрофы, нависшей над Аэтором.
            Перед героем открывается мир, полный опасности и интриг, где каждое решение будет иметь важнейшие последствия.
            Наш герой послушал старика и отправился прямиком к Запретному Храму. 
            Но вдруг из кустов на него выпригивает монстр. Это сражение научит героя драться и использовать расходники.
    """)
    heal1 = Item("средняя aптечка", 100)
    heal2 = Item("малая аптечка", 50)
    user.find(heal1)
    user.find(heal2)
#    time.sleep(5)

    m1 = Monster("∫∂∇∮∑", "∏∈", "⊂∉⊃∪∩", 100, 25)
    fight(user, m1)

    healing = int(input("Вы хотите использовать аптечку? 1 - да, 2 - нет"))
    if healing == 1:
№№№№№№№№№№№№№№№№№№№№№№№№№№№№        user.use("малая аптечка") or user.use("средняя аптечка") or user.use("большая аптечка")
        user.get_health()
    elif healing == 2:
        user.get_health()

        print(f"""Наш герой продолжает двигаться дальше, и вот опять на него нападает монстр.
         В отличие от предыдущего монстра у этого был меч и броня.
    """)
    m2 = Monster("П∇∮∑т∫∂ль", "4∏", "Т∉⊃∪а", 500, 75)
    vybor1 = int(input("1 - Вы можете сходить в данж и получить там более ценное оружие, 2 - Или попытать удачу на этом сильном монстре"))

    if vybor1 == 2:
        fight(user, m2)
    elif vybor1 == 1:
        print("Ну тогда идем в данж")

if __name__ == '__main__':
    Main()