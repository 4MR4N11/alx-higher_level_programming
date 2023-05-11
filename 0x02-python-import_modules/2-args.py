#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_num = len(argv)
    i = 1
    if args_num == 1:
        print("{} arguments.".format(args_num - 1))
    elif args_num == 2:
        print("{} argument:".format(args_num - 1))
        print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments:".format(args_num - 1))
        while i < args_num:
            print("{}: {}".format(i, argv[i]))
            i += 1
