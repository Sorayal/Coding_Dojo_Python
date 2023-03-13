"""Dies ist mehrzeiliger
Kommentar
Gut
"""

x = 1j*1J
print(x)
name = "otto"
print(name[:-1])
print(name[-2:])

print(oct(1234))
print("Hallo " + str(x)) #Interpreter wandelt x in String um
print("hallo" + " 42") #Strings verbinden

Var1 = 123
Var2 = 1.23
Var3= "Einhundert"


print(Var1,Var2,Var3, sep = "---") # Hier kann das Trennzeichen individuell definiert werden
print("|--",Var1,Var2,Var3, sep = "---")