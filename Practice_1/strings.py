course = "Python's Course for Noobs" #Double quotes to bypass apostroph error
course2 = "Python \"Noob Code\"" #double parentheses can´t be used usually within a string. With \" it´s possible
print(course2)

course3 = '''  
Hello Peter
This is a mail.
Thank you
''' #with three ' it´s possible to write a long text
print(course3)

course4 = ("Python for super noobs")
print(course4[0])
print(course4[1])
print(course4[2])
print(course4[3])
print(course4[4])
print(course4[5])
print(course4[6])
print(course4[7])
print(course4[8])
print(course4[9])
print(course4[10])
print(course4[11])
print(course4[12])
print(course4[13])
print(course4[14])
print(course4[15])
print(course4[16])
print(course4[17])
print(course4[18])
print(course4[19])
print(course4[20])
print(course4[21])
print(course4[-1]) #last character from the end

print(course4[0:6]) #gives the output between a range/ here between position 0 and 6, 6 will be excluded, so it writes 0-5
print(course4[3:6])

another = (course[:]) #copies the whole string into another variable called "another"
print(another)
name = "Jennifer"
print(name[1:-1]) #starts at first position and goes to the position before last to print the string