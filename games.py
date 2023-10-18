import time
import random

def guessthenumber():
    randomnumber = random.randint(1, 10000)
    while True:
        playernumber = int(input(">>> "))
        if playernumber > randomnumber:
            print("You Passed It")
        if playernumber < randomnumber:
            print("You Havent Passed It")
        if playernumber == randomnumber:
            print("You Won!")
        if playernumber == "break":
            break