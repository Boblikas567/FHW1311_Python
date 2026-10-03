#Перше
#users = {"Андрій": "13-15", "Супермен": "20-40", "Міша": "10-13", "Саша": "12-14"}

#name = input("Ім'я користувача: ")

#try:
#    print("Вікова група:", users[name])
#except KeyError:
#    print("НЕма такого")

#Друге
try:
    number = int(float(input("Введіть число: ")))
    print(number)
except ValueError:
    print("Неможливо перетворити")