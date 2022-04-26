#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    ldig = number % 10
else:
    ldig = number % -10

if ldig > 5:
    ifel = "and is greater than 5"
elif ldig == 0:
    ifel = "and is 0"
else:
    ifel = "and is less than 6 and not 0"

print(f"Last digit of {number} is {ldig} {ifel}")
