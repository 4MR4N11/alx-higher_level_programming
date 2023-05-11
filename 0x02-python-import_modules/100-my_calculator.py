#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, sub, mul, add
    from sys import argv
    args_num = len(argv)
    if args_num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if op != "/" and op != "+" and op != "-" and op != "*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = ".format(a, op, b), end='')
    if op == "+":
        print("{}".format(add(a, b)))
    elif op == "-":
        print("{}".format(sub(a, b)))
    elif op == "/":
        print("{}".format(div(a, b)))
    else:
        print("{}".format(mul(a, b)))
