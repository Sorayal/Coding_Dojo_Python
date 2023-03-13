def database_function(key,value): # Funktion mit 2 Parametern für den Empfang zweier Parameter
    database = {}  #Leeres Dictionary wird erstellt 
    database[key] = value #Dictionary Struktur wird erstellt
    #print (database) # Ausgabe Dictionary
    print(len(database)) 
    x=(database)
    print (database[key])
    return x


for i in range(0, 2):
    number=input("Wie lautet die erste Zahl?: ") #Wert wird in Container number gepackt
    name = input("Wie lautet der Name?: ") #Wert wird in Container name gepackt
    y = database_function (number, name) #Funktion wird aufgerufen und die zwei Container werden als Argumente an die Funktion übergeben
    print (y)
