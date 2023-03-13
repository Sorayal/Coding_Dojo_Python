zeichenkette_alt = "Halle"
zeichenkette = zeichenkette_alt.lower()

dict = {
    "a": "alewa",
    "e": "elewe"   
    }
ergebnis = ""
for x in range(len(zeichenkette)):   
    
    
    if zeichenkette[x] in dict:        
        #print(dict[zeichenkette[x]])
        ergebnis += zeichenkette[x].replace(zeichenkette[x], dict[zeichenkette[x]])
    else:
        ergebnis += zeichenkette[x]

print(ergebnis)