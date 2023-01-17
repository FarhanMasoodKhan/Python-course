# Explicit Type Conversion


# The manual conversion of one data type into another.
# Explicit type conversion is also known as Type Casting in Python.


"""
Syntax:
int(x,base)
This function can convert a floating-point number or string into an integer data type.
It consists of two parameters.

X: The first one “x” is the data type, which we want to convert into an integer data type. For example,
 if we want to write the decimal number 25 with its base, it will be written like this- (25)_{10}(25)

10: where 10 is the base for the value 25.
The second one is base, which defines the number base. For example, a binary number has a base of 2. For an octal number, the base will be 8.
The default value of the base is 10. If you want to convert the string data type into a decimal number, you need the base value to be 10.
"""



# assigning string to x
str = "0010101"
#string type casted to int base 2
base_two = int(str,2)
#default base value 10
base_ten = int(str)
print("Type casted into base 2 :",base_two)
print("Type casted into default base value 10: ",base_ten)
