class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, вік: {self.age} років"

    def eat(self):
        print(f"{self.name} їсть.")

    def sleep(self):
        print(f"{self.name} спить.")


class Mammals(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def walk(self):
        print(f"{self.name} ходить.")

    def make_sound(self):
        print(f"{self.name} видає звук.")


class Cat(Mammals):
    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self):
        print(f"{self.name} мяукає")

    def climb(self):
        print(f"{self.name} лазить по дереву.")


class Dog(Mammals):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f"{self.name} гавкає.")

    def run(self):
        print(f"{self.name} бігає.")


class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def swim_fish(self):
        print(f"{self.name} плаває.")

    def breathe(self):
        print(f"{self.name} дихає.")


class GoldFish(Fish):
    def __init__(self, name, age):
        super().__init__(name, age)

    def swim_goldfish(self):
        print(f"{self.name} плаває.")

    def hide(self):
        print(f"{self.name} ховається за рослинами.")


cat = Cat("Мурзик", 3)
dog = Dog("Бобік", 5)
fish = Fish("Стара риба", 67)
goldfish = GoldFish("Золота риба", 1)

print(cat)
print(dog)
print(fish)
print(goldfish)

cat.eat()
cat.meow()

dog.run()
dog.bark()

fish.swim_fish()
fish.breathe()

goldfish.swim_goldfish()
goldfish.hide()