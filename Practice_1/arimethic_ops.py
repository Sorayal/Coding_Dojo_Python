import time
import os

print (10/3) #gives a float number
print(10//3) # gives an integer
print (10%3) #modulo operator, returns the remainder of a division: 10 / 3 = 3 Remainder 3
print (10**3) # exponent function , 10 power 3 returns 1000 / 10 * 10 * 10

x=10
y=10
print("x= " + str(x) + " y= " + str(y)) #Multiple variable expression
x=x+3 #x increments 3
print("x=",x)
y+=3 # augented assign operator
print("y=",y)

z=20
z-=6
print(z)

time.sleep(5) # Five seconds delay
os.system("clear")
#clear = "\n" *100 
#print (clear)

#Order of operations
x=10+6/2
print(x)