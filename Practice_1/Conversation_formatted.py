#!/usr/bin/python3
#converses a number to different formats

Zahl = int(input("Please enter a number "))
print("Dezimal\tOktal\tHexdez\tBinär")
print(int(Zahl), oct(Zahl), hex(Zahl), bin(Zahl), sep = "\t")