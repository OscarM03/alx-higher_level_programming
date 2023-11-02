#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    from calculator_1 import add, sub, mul, div

    length = len(argv)
    less_arg = "Usage: ./100-my_calculator.py <a> <operator> <b>"

    if length != 4:
        print("{}".format(less_arg))
        sys.exit(1)

    not_operator = "Unknown operator. Available operators: +, -, * and /"
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        c = add(a, b)
        print("{} + {} = {}".format(a, b, c))
        sys.exit(1)
    elif argv[2] == '-':
        c = sub(a, b)
        print("{} - {} = {}".format(a, b, c))
        sys.exit(1)
    elif argv[2] == '*':
        c = mul(a, b)
        print("{} * {} = {}".format(a, b, c))
        sys.exit(1)
    elif argv[2] == '/':
        c = div(a, b)
        print("{} / {} = {}".format(a, b, c))
        sys.exit(1)
    else:
        print("{}".format(not_operator))
        sys.exit(1)
