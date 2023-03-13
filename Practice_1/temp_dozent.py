#Defininition von Start- und Endwert, Inkrement , Muss noch angepasst werden.
Celsius = 0
End_Wert = 0
Inkrement = 10


print("°C","F", sep="\t")

for TC in range(Start_Wert, End_Wert + 1, Inkrement):
    
    print(TC,TC*1.8+32)