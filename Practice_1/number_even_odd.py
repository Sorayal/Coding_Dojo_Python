#!/usr/bin/env python

Anfangswert = int(input("Bitte Anfangswert eingeben: "))
Endwert = int(input("Bitte Endwert eingeben: "))
while(Endwert < Anfangswert):
    Endwert = int(input("Der Endwert muss grösser als der Anfangswert sein. Bitte neuen Endwert eingeben: "))
for i in range(Anfangswert, Endwert+1, 1):
    if (i % 2 == 0):
        print (i, "\teven")
    else:
        print(i,"\todd")

