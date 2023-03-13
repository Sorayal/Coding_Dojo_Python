#!/usr/bin/python3

X = int(input("Gib mal ne Zahl ein: "))

while X > 0:
    if X % 2 == 0:
        print("Null")
    else:
        print("Eins")
    X = X >> 1