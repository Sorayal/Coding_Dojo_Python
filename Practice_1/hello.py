from turtle import *
shape("turtle")

x = 0
y = 0
step = 10

while 1:
    if x == 200 or x == -200:
        step *=-1
    x = x + step
    goto(x,0)
   
   


