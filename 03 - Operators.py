
print('______________________________________')
#  `Operators`
# 1 - Arithmetic Operators:  +  -  *  /
print('---Arithmetic Operators---')

a = 10
b = 2
print(2+10, a-b, 10*2, a/b) # 12 8 20 5.0



print('______________________________________')
# 2 - Assignment Operators:  =  +=  -=
print('---Assignment Operators---')

a1 = 20
print(a1) # 20
a1 += 10  # it will add 10
print(a1) # 30
a1 -= 30  # it will sub 30
print(a1) # 0


print('______________________________________')
# 3 - Comparison Operators:  < <= > >= == !=
print('---Comparison Operators---')

b1= 10 < 5
print(b1)
b2= 10 > 5
print(b2)
b3= 10 <= 10
print(b3)
b4= 10 >= 9
print(b4)
b5= 10 == 10
print(b5)
b6= 10 != 10
print(b6)

print('______________________________________')
# 4 - Logical Operators:  AND OR NOT
print('---Logical Operators---')

# AND: return True when both True
# OR: return True when anyone True
# NOT: return inverse of value
bool1 = True
bool2 = False
bool3 = True
print(" Value of Bool 1 and 2: ", bool1 and bool2)
print(" Value of Bool 1 or 2: ", bool1 or bool2)
print(" Value of not Bool 1  ", not bool1)
print(" Value of not Bool 2  ", not bool2)


print('______________________________________')
# 5 - Identity Operators:  'is'  'is not'
print('---Identity Operators---')

i1 = 10
i2 = 11
print('value of i1 is i2: ', i1 is i2)
print('value of i1 is not i2: ', i1 is not i2)


print('______________________________________')
# 6 - Membership Operators:  'in'  'not in'
print('---Membership Operators---')

m = {1,2,3,4,5,6}
print('{1,2,3,4,5,6}')
print('"5" in m: ', 5 in m)
print('"0" Not in m: ', 5 in m)
print('"0" in m: ', 0 in m)
print('"5" Not in m: ', 5 not in m)



print('______________________________________')
# 6 -  BITWISE Operators:  ' & | ^ ~ << >> '
# 'AND &'  'OR |'  'XOR ^'  'NOT ~'  'Zero Lshift <<'  'ZRS >>'
print('--- BITWISE Operators---')


print('AND: Sets each bit to 1 if both bits are 1 else 0')
ba1 = 4  # 0100 in binary
ba2 = 3  # 0011 in binary
#        = 0000
# [ (0*2)^3 + (0*2)^2 + (0*2)^1 + (0*2)^0 ] = 0
print("AND operation: ", ba1 & ba2)


print('OR: Sets each bit to 1 if one of two bits is 1')
ba1 = 4  # 0100 in binary
ba2 = 3  # 0011 in binary
#        = 0111
# [ (0*2)^3 + (1*2)^2 + (1*2)^1 + (1*2)^0 ] = 7
print("OR operation: ", ba1 | ba2)



print('XOR: Sets each bit to 1 if only one of two bits is 1')
ba1 = 4  # 0100 in binary
ba2 = 3  # 0011 in binary
#        = 0111
# [ (0*2)^3 + (1*2)^2 + (1*2)^1 + (1*2)^0 ] = 7
print("XOR operation: ", ba1 ^ ba2)



print('NOT: Inverts all the bits')
ba1 = 4  # 0100 in binary
#        = 1011
# [ (1*2)^3 + (0*2)^2 + (1*2)^1 + (1*2)^0 ] = -5
print("NOT operation: ", ~ba1)




print('ZERO FILL LEFT SHIFT'
':Shift left by pushing zeroes in from the right '
'and let the leftmost bits fall off')
ba1 = 4 # 00100 in binary
#       = 01000  <- fill with 0 bit to move value towards LS
# [  (0*2)^4 + (1*2)^3 + (0*2)^2 + (0*2)^1 + (0*2)^0 ] = 8
print("<< operation: ", ba1 << 1 )   # shift left by 1 bit


print('# ZERO FILL RIGHT SHIFT:'
'Shift right by pushing copies of the leftmost bit in from the'
'left and let the rightmost bite fall off')
ba1 = 4 # 00100  in binary
#       = 00010  fill with 0 bit to move value towards RS ->
# [  (0*2)^4 + (0*2)^3 + (0*2)^2 + (1*2)^1 + (0*2)^0 ] = 2
print(">> operation: ", ba1 >> 1 )