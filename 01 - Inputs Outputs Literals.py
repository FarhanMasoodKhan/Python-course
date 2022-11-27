#      ----------    INPUTS        ----------

intro = input('username:  ')
print('Hey there', intro)

lang = input(' Enter your favorite language: ')
print('Yeah {} is the most Popular language'.format(lang))

age = int(input("Enter your age: "))
print(' so your are ' + str(age) + ' years old')

cgpa = float(input("What is your CGPA: "))
print('wow your cgpa '+ str(cgpa) + ' is amazing')
print('______________________________________')




# --------   OUTPUT    -----------

print(0, 1, 2, 3, 4)    #simple :  1 2 3 4 5
print(0, 1, 2, 3,  sep='-')      # with separations  1-2--3-4-5
print(1, 2, 3, 4, sep='~', end='** ')    #with sep and End   1-2-3-4-5**
print(""" milti
             line
                print""")


print('______________________________________')
print('We can print a string and number together')
students = 5000
# str(students) is to convert int value into string
print("Python  has " + str(students) + 'k' + " downloads")


print('______________________________________')
print("Here we take two variables and do certain operations with it")
x = 2
y = 10
ans = x * y
# Formatting values
print('The value of y is {} and x is {}'.format(y, x))
# Here we are specifying the order of the variables.
print('{2} is the multiplication of {0} and {1}'.format(x, y, ans))

# We can even use keyword arguments to format strings.
print('Hey! I am {name} and I like {language}'.format(name='Farhan', language='Python'))
print('______________________________________')







#---------    Literals in Python     ------------
print("------------LITERALS--------------")
""" Types of Literals in Python
1. String Literals
2. Numeric Literals
3. Boolean Literals
4. Literal Collections
5. Special Literals
"""
# --------------   1 . String Literals  ------------

# a) Single-line String: String literals that are enclosed within single quotes (‘’) are known as single-line strings.
single_quotes_string='Learn Python'
double_quotes_string="Hello World"
print(single_quotes_string)
print(double_quotes_string)

# b)  Multi-line String:
multiline1="""This is
multi line
string"""
print(multiline1)

multiline2="This is\
 multi line\
 String\
"
print(multiline2)
print('______________________________________')


#  _________    Numeric Literal  __________
# A - Integer
#positive whole numbers
#>>  x = 2586
#negative whole numbers
#>>  y = -9856

# 1- Decimal- It contains digits from 0 to 9. The base for decimal values is 10.
#> >  b = 505

# 2- Binary- It contains only two digits- 0 and 1. The base for binary values is 2 and prefixed with “0b”.
#>>  a = 0b10101

# 3- Octal- It contains the digits from 0 to 7. The base for octal values is 8. In Python, such values are prefixed with “0o”.
#>>  c = 0o350

# 4- Hexadecimal- It contains digits from 0 to 9 and alphabets from A to F.
#>>  d = 0x12b


# B - Float Literals --
# Types: A. Fractional- Fractional literals , Exponential- Exponential literals
print('Flaot value is ',78.256)  # 78.256


# C - Complex Literals  ---
"""Complex literals are represented by A+Bj.
    Over here, A is the real part. And the entire B part, along with j, is the imaginary or complex part.
    'j' here represents the square root of -1, which is nothing but the IOTA or i we use in Mathematics."""

#>  a=7 + 8j
#>  b=5j
#>  print(a)
#>  print(b)
print('______________________________________')




# -----------    Boolean Literals   --------------
"""
True- True represents the value 1.
False-False represents the value 0.
"""
print('______________________________________')


#-------------   Special Literals     --------------
"""  Python literals have one special literal known as None.
This literal in Python is used to signify that a particular field is not created. """
val=None
print(val) 	 #None
print('______________________________________')


# ------------   Literal Collections  ------------------
#--    i)   List Literals
"""
Lists are a collection of data declared using the square brackets([]) and commas separate the elements of the list (,) 
 list Literals are mutable.  """
numbers = [10, 20, 30, 40, 50]
names = ['John', 'Jake', 'Jason', 25]
print(numbers)   # [10, 20, 30, 40, 50]
print(names)    # ['John', 'Jake', 'Jason', 25]

# --    ii)   Tuple Literals  --
"""
The literals that are declared using ( ) brackets and can hold any datatype are tuples. Tuples are immutable.
"""
even_numbers = (2, 4, 6, 8)
vowels=('a','e','i','o','u')
print(even_numbers)   # (2, 4, 6, 8)
print(vowels)      # ('a', 'e', 'i', 'o', 'u')

#--  iii) Dictionary Literals  --
"""
Dictionary is a collection of data that stores value in a key-value format. Dictionaries are mutable 
var = { 'key': 'value' }
"""
my_dict = {'a': 'apple', 'b': 'bat', 'c': 'car'}
print(my_dict)	# {'a': 'apple', 'b': 'bat', 'c': 'car'}


#--  iv) Set Literals  --
"""Set literals are a collection of unordered data that cannot be modified."""
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)    # {'o', 'e', 'a', 'u', 'i'}