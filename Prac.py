x = .3
if x > 1 :
    print ('True')
elif x < 1 :
    print ('false')

x = 10068
y = 100
if x > y :
    print (x)
elif y > x :
    print (y)
else :
    print ("x and y are equal")

x = 8

if 0 < x and x < 10:
        print ('x is a positive single-digit number.')

import math 

import random
for i in range(10) :
     x = random.random()
     print(x)


x = random.randint(1,2000)
print (x)

def print_twice(blah):
     print(blah)
     print(blah)
exam = "this is cool"
print_twice(exam *3)

def addtwo(a, b):
     added = a + b
     return added
x = addtwo(7, 10)
print(x)

x = 15
x = x * 5
print (x)

n = 5
while n > 0:
     print(n)
     n = n - 1
print ('blastoff!')



friends = ['Joe', 'Sam', 'Dean']
for friend in friends:
     print('happy New Year:', friend)
print('Done!')

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
     count = count + 1
print('Count', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
     total = total + itervar
print('Total:', total)

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
          largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest) 

largest_so_far = 1
print('Before', largest_so_far)
for the_num in [3, 56, 142,2]:
     if the_num > largest_so_far :
          largest_so_far = the_num 
     print(largest_so_far, the_num)
print('after', largest_so_far)

x = "cybersecurity"
pos = x.find('ec')
print(pos)

cyberwords = list(['hack','cyber','pentest'])
x = 'hacks' in cyberwords
print(x)