import random
from random import randint

# All uppercase password
password = ""
for i in range(10):                       # 10 character password
    a = chr(randint(65, 90))              # letter A - Z (uppercase)
    password = str(password) + a          # Take the empty string and add a random letter 10x
print("Password suggestion:", password)


# Uppercase and lowercase password
password = ""
for i in range(5):                        # 5 upper case characters
    a = chr(randint(65, 90))
    b = chr(randint(65, 90)).lower()      # 5 lowercase characters
    password = str(password) + a + b
print("Password suggestion:", password)


# Uppercase, lowercase and integer password
password = ""
for i in range(3):
    a = chr(randint(65, 90))
    b = chr(randint(65, 90)).lower()
    c = str(randint(0, 9))
    password = str(password) + a + b + c
print("Password suggestion:", password)


# Upper, lowercase and numbers password then shuffled
password = ""
for i in range(3):
    a = chr(randint(65, 90))
    b = chr(randint(65, 90)).lower()
    c = str(randint(0, 9))
    password = str(password) + a + b + c

list1 = random.sample(password, len(password))           # stores lists
shuffled_password = "".join(list1)                       # turns list to string
print("Password suggestion:", shuffled_password, '\n')   # prints new shuffled password


# Upper, lowercase, numbers and special characters then shuffled
password = ""
for i in range(3):
    a = chr(randint(65, 90))
    b = chr(randint(65, 90)).lower()
    c = str(randint(0, 9))
    d = chr(randint(*random.choice([(33, 47), (58, 64), (91, 96), (123, 126)])))
    password = str(password) + a + b + c + d

list1 = random.sample(password, len(password))
shuffled_password = "".join(list1)
print("Here is your final password:", shuffled_password)
