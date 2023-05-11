#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    a = 10
    b = 5
    print("{:s} + {:s} = {:s}".format(str(a), str(b), str(add(a, b))))
    print("{:s} - {:s} = {:s}".format(str(a), str(b), str(sub(a, b))))
    print("{:s} * {:s} = {:s}".format(str(a), str(b), str(mul(a, b))))
    print("{:s} / {:s} = {:s}".format(str(a), str(b), str(div(a, b))))
    