#formatted strings
first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder"
msg = f"{first} [{last}] is a coder" #formatted string , between {} it creates holes/placeholder for variables, prefix f
print(message)
print(msg)