#!/usr/bin/python3
A = "Hallo Welt Welt"
print(A.find("al"))  #returns an index value, Index position
print(A.find("We"))  #A before dot is the position where to search
print(A.find("We",7)) #searchs for the next index
print(A.find("We", A.find("We") + 1))

print(len(A)) #its a function, not a method, finds the length

