import random

class Human:
    def __init__(self, name, car=None):
        self.name = name
        self.car = car
        self.house = House("Квартира")
        self.gladness = 30
        self.energy = 30
        self.money = 1000
        self.alive = True

    def work(self):
        print(f"Ну дуже тяжка праця.")
        self.money += random.randint(300, 500)
        self.energy -= 5
        self.gladness += 1

    def shopping(self):
        self.money -= random.randint(20, 50)
        self.house.food += random.randint(1, 10)
        if self.car == None:
            print("Пішов на шопінг пішки")
        else:
            if self.car.drive(random.randint(10, 20)):
                print("Поїхав на шопінг на авто")
            else:
                print("Немає бензину, пішов пішки")

    def eat(self):
        print(f"Яка смачна їжа.")
        self.energy += 4
        self.gladness += 3
        self.house.food -= 1

    def chill(self):
        print(f"Подобається мені відпочивати.")
        self.energy += 7
        self.gladness += 5

    def cleaning(self):
        print(f"Скоро буде чистий дім.")
        self.energy -= 2
        self.gladness += 2
        self.house.pollution -= 1

    def rich(self):
        if self.money >= 10000:
            self.car = Car("BMW")
            self.house = House("Будинок")
            self.gladness += 10
        if self.money >= 20000:
            self.car = Car("Lamborghini")
            self.house = House("Особняк")
            self.gladness += 20

    def info(self):
        print(f"Сьогодні {self.name} має:")
        print(f"Задоволення : {self.gladness}")
        print(f"Машина      : {self.car}")
        print(f"Енергія     : {self.energy}")
        print(f"Гроші       : {self.money}")
        print(f"Дім         : {self.house}")


    def is_alive(self):
        if self.gladness <= 0:
            print(f"Більше не хочу жити :(")
            self.alive = False
        if self.energy <= 0:
            print(f"Я більше не можу працювати.")
            self.alive = False
        if self.money >= 50000:
            print(f"Я дуже богатий, мені не потрібна робота!")
            self.alive = False

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-" * 30)


        func = [self.work, self.shopping, self.eat, self.chill, self.cleaning]
        random.choice(func)()

        self.info()
        self.is_alive()
        self.rich()
        print()

    def party(self):
        print(f"Танцуємо друзі!!")
        self.energy -= 2
        self.gladness += 3
        self.house.pollution += 2


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel > 0:
            print(f"Ми проїхали {length} км, виратили {delta_fuel} л пального")
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            return True
        else:
            print("Подорож неможлива, не вистачає пального")
            return False

    def add_fuel(self):
            if self.money >= 100:
                self.money -= 100
                self.fuel += 1
                if self.fuel > 60:
                    self.fuel = 60

    def __str__(self):
        return f"Авто: {self.model}, пальне: {self.fuel} л, стан {self.state} %"

class House:
    def __init__(self, type):
        self.type = type
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"Дім: {self.type}"

human = Human("Андрій")
for day in range(365):
    if not human.alive:
        break
    human.live(day)
