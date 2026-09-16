class Cat:
    def __init__(self, name, age, height, breed):
        self.name = name
        self.age = age
        self.height = height
        self.breed = breed

    def __str__(self):
        return f"У мене є кіт {self.name}, йому {self.age} років, його зріст {self.height} см, і його порода {self.breed}.\n"
    def __del__(self):
        print(f"{self.name} пішов на вулицю.")

cat = Cat("Барсік", 2, 25, "Сфінкс")
print(cat)
