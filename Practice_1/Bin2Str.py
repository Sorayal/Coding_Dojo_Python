#!/usr/bin/python3
number=int(input("Bitte geben Sie eine beliebige positive Zahl ein "))
while number <= 0:
    number=int(input("Bitte geben Sie eine beliebige positive Zahl ein "))
   
print (bin(number))
bin_number = (bin(number))

while number >0:
    if(number & 1) == 1:
        print("1")
    else:
        print("0")
    number = number >> 1
    
    
    
"""while x > 0:
    if x%2 == 0:
        print("null")
    else:
        print("eins")
    x=x>>1"""

#for digit in (str(bin_number)):
    
    #print(digit)