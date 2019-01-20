from random import randint, choice
from calc import eval


x = randint(0, 10)
y = randint(1, 10)
op = choice(["+","-","*","/"])
error = randint(-1, 1)
r = eval(x, y, op) + error


print(x, "+", y, "=", r)

user_input = input("Your answer (Y/N").upper()

result = ""
if error == 0:
    if user_input == "Y":
        result = "Yay"
    else:
        result = "Nay"
else:
    if user_input == "Y":
        result = "Nay"
    else:
        result = "Yay"

print(result)       