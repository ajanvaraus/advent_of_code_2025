# part 1
f = open("input_day_1.txt")
line = f.readline()
pos = 50
total = 0

while (line != "") :
    turn = int(line[1:])
    if (line[0] == 'R') :
        pos = pos + turn
    elif (line[0] == 'L') :
        pos = pos - turn   
    
    while (pos < 0) :
        pos = 100 + pos
    while (pos > 99) :
        pos = pos - 100
    
    if (pos == 0) :
        total += 1
    line = f.readline()

print(total)

f.close()

# part 2

f = open("input_day_1.txt")
line = f.readline()
pos = 50
total = 0

while (line != "") :
    dir = line[0]
    turn = int(line[1:])

    for i in range(turn):

        if (dir == 'L'):
            pos -= 1
        elif (dir == 'R'):
            pos += 1

        if (pos == 100):
            pos = 0
        if (pos == -1):
            pos = 99

        if (pos == 0):
            total += 1

    line = f.readline()
print(total)

f.close()


