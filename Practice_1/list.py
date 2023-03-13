#!/usr/bin/python3

Liste_von_Teilnehmern = ["Hugo","Karl","Else","Sina"]
Liste_von_Teilnehmern.append("Paula") #Hinzufügen von einem Listenelement
print(Liste_von_Teilnehmern)
print(Liste_von_Teilnehmern[2])
print(Liste_von_Teilnehmern[1:3])
print(Liste_von_Teilnehmern[-3:])
print(len(Liste_von_Teilnehmern))

if "Hugo" in Liste_von_Teilnehmern: #Abfrage, ob ein Teilnehmer vorhanden ist
    print("True")
    
    
#Daten.join(Liste_von_Teilnehmern,",") #kreiert eine CSV für den Austausch
#Liste_von_Teilnehmern = Daten.split(",") #wandelt die CSV wieder in eine Liste
    

Telefon ={"Kurt":"1234","Hugo":"5678"}
print(list(Telefon.keys()))
