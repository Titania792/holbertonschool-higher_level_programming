#!/usr/bin/python3
for numbers in range(99):
    print(f"{numbers:02d}, ", end="")
    if numbers == 98:
        print(f"99")
        break
