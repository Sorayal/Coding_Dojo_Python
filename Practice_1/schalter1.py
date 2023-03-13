#!/usr/bin/python3

Tasterzahl=int(input("Gib mal ne Zahl ein: "))
print("Zum Vergleich das Binärmuster:", bin(Tasterzahl))

Maske = 0x18 #
if Tasterzahl & Maske == 0x18: 
    print("Bumm!")
else:
    print("Das ging noch mal gut ;) ")