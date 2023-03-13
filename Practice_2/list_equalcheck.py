#!/usr/bin/python3
all_the_same = []
counter = int(input("How many items do you want to place into the list? "))

for i in range (counter):
    item = input("Enter the name or number of the item:  ")
    all_the_same.append(item)

print(all_the_same)
i = 0
while i < (len(all_the_same)):
    if all_the_same[0] !=all_the_same[i]:
        bool = False
        break
    else:
        bool = True
        i+=1

print("all_the_same (%s) == %s" %(all_the_same,bool))

if bool == True:
    print("True")
else:
    print("False")