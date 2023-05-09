#!/usr/bin/python3
for i in range(0, 99):
    print("{:s}".format(str(i).zfill(2)), end=', ')
print("{:s}".format(str(i + 1).zfill(2)))
