fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print ('Line Count', count)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    #skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    #Process our 'interesting' line
    print(line)

    x = []

    print(x)