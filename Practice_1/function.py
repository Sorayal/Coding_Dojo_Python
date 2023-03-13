#!/usr/bin/python3
# example for functions

def C2F(Celsius):                #C2F function name (Celsius parameter)
    """A unit conversation from Fahrenheit to Celsius"""
    return Celsius * 1.8 +32     #short version of Fahrenheit = Celsius * 1.8 +32 / return Fahrenheit

def C2K(Celsius):
    """A unit conversation from Celsius to Kelvin"""
    return Celsius + 273.15

def printf(x):
    print(x)
    

for C in range (0,101,10):       #C new variable to contain the return value of the function
    print(C,"°C", C2F(C),"°F", C2K(C),"K", sep = "\t") #sep = "\t" Separator between variables

printf("\nThe automatic documentation for C2F\n" + C2F.__doc__) #using the printf instead of print 