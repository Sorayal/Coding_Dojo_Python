#!/usr/bin/python3
import random
random.seed()

countrylist = {"Italien":"Rom", "Belgien":"Bruessel","Niederlande":"Amsterdam","Luxemburg":"Luxemburg",\
               "Frankreich":"Paris","Deutschland":"Berlin"}
print("Hello and welcome for the quiz about the capitals of the world.\nYou will be asked for a capital of a specific country.\nHave fun.")
print("\n"*2)
rounds = int(input("How many rounds do you want to play? The maximum are %i rounds." % len(countrylist)))
print(len(countrylist))
points = int(0)
i = 0
country_keylist=list(countrylist.keys())
#print(Landesliste[ListeL[4]])

while (i<rounds):
    index=random.randint(0,len(country_keylist)-1)
    antwort=input("\nWhat is the capital of %s ?" % (country_keylist[index])) # %s will be filled with the string from the indexposition which is diced before.
    if antwort == countrylist[country_keylist[index]]:  #looks if the answer is equal to the indexposition of the country_keylist which relates to the countrylist.
        print("\nYou´re right. :)")
        points +=1
    else:
        print("\nWrong. The answer is %s" % countrylist[country_keylist[index]])
    
    country_keylist.pop(index)     #deletes one element from the keylist and it´s related to the random index which is diced before.
    #print (land_keylist)
    i+=1  
print("\nYou have reached %i points." %points)