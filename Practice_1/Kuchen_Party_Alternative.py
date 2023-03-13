#!/usr/bin/python3

Kuchenstücke=int(input("Anzahl der Kuchenstücke: "))
Teilnehmer=int(input("Anzahl der Teilnehmer: "))

print("Du musst " + str(Kuchenstücke % Teilnehmer) + " Stücken wegnehmen")
print("Jeder Teilnehmer erhält dann " + str(Kuchenstücke // Teilnehmer) + " Kuchenstücke")