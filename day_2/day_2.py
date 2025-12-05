# part 1
f = open("input.txt")
input = f.readline()

temp = ""
low = 0
high = 0

sum = 0

for k in range(len(input)):
    i = input[k]
    if (i == '-'):
        low = int(temp)
        temp = ""
    elif (i == ',' or k == len(input)-1) :
        high = int(temp)
        temp = ""
        for j in range(low, high + 1) :
            string = str(j)
            x = string[:len(string)//2]
            y = string[len(string)//2:]
            if (x == y) :
                sum += j
    else :
        temp += i
print(sum)

# part 2, input stolen from first one

def sequences(step, numStr) :
    list = []
    match = True

    while len(numStr) >= step :
        list.append(numStr[:step])
        numStr = numStr[step:]

    if (len(numStr) > 0 or len(list) == 1) :
        match = False
    else :
        for i in range(1,len(list)) :
            if (list[i] != list[i-1]) :
                match = False

    return match

def finder(numStr) :
    match = False
    for i in range(1, (len(numStr)//2)+1) :
        if (not match and sequences(i,numStr)) :
            match = True

    return match

temp = ""
low = 0
high = 0

sum = 0

for k in range(len(input)):
    i = input[k]
    if (i == '-'):
        low = int(temp)
        temp = ""
    elif (i == ',' or k == len(input)-1) :
        high = int(temp)
        temp = ""
        for j in range(low, high + 1) :
            if (finder(str(j))) :
                sum += j
    else :
        temp += i
print(sum)