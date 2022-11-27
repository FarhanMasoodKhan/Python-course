# --------   OUTPUT    -----------

print(0, 1, 2, 3, 4)    #simple :  1 2 3 4 5
print(0, 1, 2, 3,  sep='-')      # with separations  1-2--3-4-5
print(1, 2, 3, 4, sep='~', end='**')    #with sep and End   1-2-3-4-5**
print(""" milti
             line
                print""")
print(' ')


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
#      ----------    INPUTS        ----------

intro = input('username:  ')
print('Hey there', intro)

lang = input(' Enter your favorite language: ')
print('Yeah {} is the most Popular language'.format(lang))

age = int(input("Enter your age: "))
print(' so your are ' + str(age) + ' years old')

cgpa = float(input("What is your CGPA: "))
print('wow your cgpa '+ str(cgpa) + ' is amazing')