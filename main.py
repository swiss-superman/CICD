import os
import hashlib
import sqlite3

rawinput = input("input: ")
eval(rawinput)  # eval on unsanitized user input

username = input("Enter username: ")
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")  # injection

password = input("Enter password: ")
weak_hash = hashlib.md5(password.encode()).hexdigest()  # weak cryptography.

# high-entropy strings and known patterns matching credentials.
AWS_ACCESS_KEY_ID = "90546f460f8f45896a13cc9aed671c5f"
