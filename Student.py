import random

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 10
        self.gladness = 30
        self.energy = 50
        self.alive = True
        self.money = 500

    def study(self):
        print("Я пішов до академії IT STEP")
        self.progress += 1
        self.energy -= 1
        self.gladness -= 3

    def chill(self):
        print("Я пішов з друзяками гулять")
        self.gladness += 2
        self.energy -= 3
        self.progress -= 1
        self.money -= 24

    def sleep(self):
        print("Я пішов спати")
        self.energy += 3
        self.gladness += 1

    def eat(self):
        print("Чіпси та кола - наші найкращі друзі :)")
        self.energy += 1
        self.gladness += 1
        self.money -= 42

    def is_alive(self):
        if self.gladness <= 0:
            print("В мене дипресія :(")
            self.alive = False
        if self.energy <= 0:
            print("Я зовсім знесилений :(")
            self.alive = False
        if self.progress <= 0:
            print("В мене в голові суцільне сміття :(")
            self.alive = False
        if self.progress > 100:
            print("Я геній. Достроково закінчив академію IT STEP :)")
            self.alive = False
        if self.money <10:
            print(f"Друзі, не смійтесь, хватит булити мене :_(")
            self.alive = False
        if self.money < 0:
            print(f"{self.name} не віддав долги, і його більше ніхто не побачив...")

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

        func = [self.study, self.sleep, self.eat, self.chill, self.moneymaking]
        random.choice(func)()

        self.info()
        self.is_alive()
        print()

    def info(self):
        print(f"На сьогодні {self.name} має:")
        print(f"Задоволення : {self.gladness}")
        print(f"Знання      : {self.progress}")
        print(f"Енергія     : {self.energy}")
        print(f"Гроші       : {self.money}")


    def moneymaking(self):
        print(f"Можете будь ласка дати гроші?")
        self.money += 67
        self.gladness += 5


student = Student("Vasya")
for day in range(365):
    if not student.alive:
        break
    student.live(day)