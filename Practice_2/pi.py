#Pi formula V 0.1
#it needs more rework

i = 0
for i in range (2,100):
    if i>3:
        if ((i%2) and (i%3) and (i%5) and (i%7)) != 0:            
            print(i)

             

        