#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    res = 0
    for i in range(1, leng):
        res = res + int(sys.argv[i])
    print(f"{res}")
