# Implicit Type Conversion

# In Implicit type conversion, Python automatically converts
# one data type to another data type without any user's need.


num1 = 2   #int
num2 = 12.2  #float
res = num1 + num2
print("Data type of num1: ", type(num1))    # 2 - int
print("Data type of num2: ", type(num2))    # 12.2 - float
print("Data type of res: ", type(res))     # 14.2 - FLOAT
print("Value of res: ", res)               # converted to Float
# Hence, the Python compiler converted the smaller data type (int)
# into a larger one (float) to avoid any "Data loss".