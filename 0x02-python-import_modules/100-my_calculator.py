#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    num = (len(sys.argv) - 1)
    if num != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == '+':
            res = add(a, b)
        elif operator == '-':
            res = sub(a, b)
        elif operator == '*':
            res = mul(a, b)
        elif operator == '/':
            res = div(a, b)
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)

    print(f"{a} {operator} {b} = {res}")
