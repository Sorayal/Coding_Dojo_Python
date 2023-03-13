
first_value = 4
second_value = 2
# both are class int
print(type(first_value))
print(type(second_value))

result = 4 / 2
datat = type(result)
# division leads an automatic conversion to class float as datatype.
print(f"The datatye of result is {datat} and the result of {first_value} divided by {second_value} is {result}.")

# Integer Divivion
result = 4 // 2
datat = type(result)
# The integer division leads to class int a result datatypes
print(f"The datatye of result as integer division is {datat} and the result of {first_value} divided by {second_value} is {result}.")