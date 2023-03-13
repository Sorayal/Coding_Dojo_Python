#!/usr/bin/python3
print("***>" + "Hallo" + "<***")
print("***>" + "Hallo".center(7) + "<***") #space of 7 chars, centers the text
print("***>" + "Hallo".center(8) + "<***")
print("Hallo".rjust(11,"-"))
print("Hallo".rjust(11))
print("Hallo".ljust(11,"-"))


Text = ("Hallo Welt")
Trenn = "#"
Spalte = 30
print(Text.center(Spalte,Trenn))

#String modulo Method to format strings
A=123456
print("%e"%A) #formatted output as expontial form
print("%10.3f"%A) #10 spaces , it contains all digit and dot, 3 digits after dot
