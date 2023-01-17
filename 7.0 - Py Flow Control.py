# python flow control - conditions
# if, if else, if elif else,

marks = int(input("Enter Student Marks: "))
if marks >= 90 and   marks <= 100:
    print("Grade A+")
elif marks >= 80 and   marks < 90:
    print("Grade A")
elif marks >= 70 and marks < 80:
    print("Grade B")
elif marks >= 60 and marks < 70:
    print("Grade C")
elif marks >= 50 and marks < 60:
    print("Grade D")
elif marks >= 40 and marks < 50:
    print("Grade E")
elif marks < 40:
    print("Grade F")
else:
    print("Invalid Input")


# Switch Case ( match )

color = int(input("Put color code: "))

match color:
    case 0:
        print("red")
    case 1:
        print("blue")

car = input("Car Name: ")

match car:
    case "honda":
        print('2022')


# While Loop

i = 1
j = 1
while i <= 10:
    print("Farhan")
    i += 2
    while j <= 5:
        print("masood")
        j += 1
        break
else:
    print("Name Printed")

# Here, the expression count != 1 is always True. So the body of the while loop is executed on infinite.
i = 0
while i != 1:
    name = str(input("Name bol: "))
    print(" han bey " + name)

# here  "continue" means skipping this iteration at  'count == 2'
# if we put "break" instead of continue : iteration will stop 'count == 2'
count = 0
while count < 5:
 count += 1;
 if(count == 2): continue
 print("The value of the count is " + str(count))

# ----------------------     Examples  ----------------------------
# Fibonacci Series Example
itr = 0
n1 = 0
n2 = 1

while itr < 10:
    print(n1)
    next = n1 + n2
    n1 = n2
    n2 = next
    itr = itr + 1

# Even Odd
i = 0

while i <= 10:
        if i % 2 == 0:   #     == 1  for Odd
            print("Even Num is: ", i)
        else:
           print("Odd num")
        i += 1
# ------------------------------------------------------------

# Range
# range( start , end , jump )      i.e   range(n) means by default 'start=0' and 'jump=1'

# keypoint: always neglet last integer
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  means  'end at 10' by default 1 increment

list(range(1,10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]   means (start at 1)  (end at 9) by default increment 1

list(range(1,10,2))
# [1, 3, 5, 7, 9]   means 1 to 10 by increment of 2

list(range(10,1,-1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2]   by decrement 1  ( 10 to 2)



# FOR LOOP

i = 0
n = int(input("Table of: "))

for i in range(1,11):
    print(i*n)


# --------------------------
#  BREAK: Break flow of program if condition hit
#  CONTINUE: skip particular iteration
#  PASS: to avoid syntax error
