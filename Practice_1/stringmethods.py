#string methods
course = "Python for beginners"
print(len(course)) #string length, it counts the characters in a string/ starting with 1
# len is a general purpose function
print(course.upper()) # with dot . you can enter the functions/methods which are related to strings. Here it creates a new string which is uppercase.
print(course.lower()) #creates a new string, which is lowercase
print(course) #the variable didn´t changed really

#Functions which are related to something specific or related to an objects are called methods.
#Functions which are general purpose function, are not related to anything specific


print("\t")
print(course.find("P")) #It gives the index number where the searched character is. If the method can´t find anything, it will wrote -1. It´s case-sensitive
print(course.find("beginners")) #beginners start at position 11
print(course.replace("beginners", "supernoobs")) #replaces beginners with Supernoobs
print("Python" in course) #Asks, if a sequence of characters is there and gives a boolean as feedback



