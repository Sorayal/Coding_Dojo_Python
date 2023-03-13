#!/usr/bin/python3

Kuchenstücke=input("Anzahl der Kuchenstücke: ")
Teilnehmer=input("Anzahl der Teilnehmer: ")
Stücke = int(Kuchenstücke) % int(Teilnehmer) #type-conversation necessary from string to int
print("Du musst " + str(Stücke) + " Stücken wegnehmen")
Verteilung_Kuchenstücke = int(Kuchenstücke) // int(Teilnehmer)
print("Jeder Teilnehmer erhält dann " + str(Verteilung_Kuchenstücke) + " Kuchenstücke")