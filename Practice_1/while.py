number = int(input("Please enter a number"))
while number>0:
    abfrage=input("Do you want to continue? (n for Exit, j for Continue)").lower()
    if abfrage == "n":   #Doppelpunkt muss immer eingegeben werden!!! Kein Continue hinter if
        break
    if abfrage != "j":
        print("Please press j-Key to Continue,n-Key for Exit")
        continue #Jumps at the start of the while loop
    number-=1
    print(number)