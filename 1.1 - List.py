#  List
# List items are ordered, changeable, and allow duplicate values.

cName = [ 'Farhan', 'Neshaf', 'wamik', 'sameer', 'umar']
cAge = [24, 21, 19, 16, 15]

print(cName)            # [ 'Farhan' ...... ]
print(cAge)               # [24, 21..........]
print(cName[0])         # Farhan
print(cName[-1])        # umer - reverse index
print(cName[2:4])      # ['wamik', 'sameer']
print(cName[:3])        # ['Farhan', 'Neshaf', 'wamik']
print(cName[3:])        # ['sameer', 'umar']

if "Farhan" in cName:
    print('item found in list')
else:
    print('Not fount')

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)