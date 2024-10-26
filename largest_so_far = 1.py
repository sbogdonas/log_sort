largest_so_far = -1
print('Before', largest_so_far)
for the_num in [3, 56, 142,2]:
     if the_num > largest_so_far :
          largest_so_far = the_num 
     print(largest_so_far, the_num)
print('after', largest_so_far)

fruit = 'apple'
letter = fruit[1]
print(letter)

temp = 'no_way'
length = len(temp)
print(length)
last = temp[length-1]
print(last)

index = 0
while index < len(temp):
     letter = temp[index]
     print(letter)
     index = index + 1

index = len(temp) - 1

while index >= 0:
     print(temp[index])
     index -= 1

for char in temp:
     print(char)

s = 'Monty Python'
print(s[:4])
print(s[6:])

greeting = 'Hello world'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

word = 'cant be, no way'
new_word = word.find('b')
print(new_word)

word = 'banana'
letter_count = word.count('a')
print(letter_count)

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)



