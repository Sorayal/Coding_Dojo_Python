# Runnable with Python 3.9
# Python is a dynamic-typed language.


# Some simple calculations
v = 3
x = 4
print(v * x)
print(v ** x)
print(v + x)
print(v - x)
print(3 * "\n")

print("Are all chars in this string ASCII-Chars? " + str(bin(v).isascii()))

# String Interpolation with f-string
print(f"The hex value of{v} is " + hex(v))

print(bin(v) + hex(v))
print(v)
print(3 * "\n")

# Some strings and operations
firstString: str = "It`s a new world. \n"
secondString = "Have fun with exploring it!"
print(firstString + secondString)
print(firstString.__contains__("o"))
