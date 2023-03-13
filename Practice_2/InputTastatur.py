#Grundlagen Eingabe
#Funktion Input

Name = input("Wie heisst du?")
print("Du hast", Name,"gesagt")
print(3*"\n")


#Cast auf int und try/except
try:
    text = 3
    zahl = int(text)
    print(3*zahl)
except ValueError:
    print("Falsche Eingabe: ",text)
    
    