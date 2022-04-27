#!/usr/bin/python3
numbers = 0
for fdig in range(9):
    numbers = numbers + 1
    for sdig in range(numbers, 10):
        print(f"{fdig}{sdig}, ", end="")
print(f"89")
