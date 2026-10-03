import sqlite3

connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT, email TEXT)")

for i in range(3):
    login = input("Login: ")
    password = input("Password: ")
    email = input("Email: ")
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", (login, password, email))

connection.commit()
connection.close()