#!/usr/bin/python3
# control structures
#A script to check for leap-years

Year = int(input("Please enter a year: "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("This year is a leap-year")
        else:
            print("This year is not a leap-year")       
    else:
        print("This year is a leap-year.")
else:
    print("This is not a leap-year")