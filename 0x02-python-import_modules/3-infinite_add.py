#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    args_num = len(argv)
    result = 0
    if args_num == 1:
        print("0")
    else:
        while i < args_num:
            result += int(argv[i])
            i += 1
        print("{}".format(result))
