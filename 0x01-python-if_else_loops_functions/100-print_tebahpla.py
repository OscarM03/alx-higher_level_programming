#!/usr/bin/python3
for c in range(ord('z'), ord('a')-1, -1):
    if c % 2 == 1:
        char = c - 32
    else:
        char = c
    print("{}".format(chr(char)), end="")
