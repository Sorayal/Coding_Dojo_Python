#initialize
my_list = [1,2,3,":)", True, 4.5] #kist can contain several datatypes

#add item
my_list.append(89)
print(my_list)

#access item
print (my_list[3]) #print the item with the indexnumber 3

#change item
my_list[3] = ":D"
print (my_list[3])

#remove item by index
del my_list[3]
print(my_list)

#iterate
for item in my_list:
    print item