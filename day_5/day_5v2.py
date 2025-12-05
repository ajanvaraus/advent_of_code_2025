# PART 2

# all fresh id's
# rangeToArray function
# gets array of ranges ["1-4","2-6",...]
# return list of two arrays
def rangeToArray(input) :
    lowRange = []
    highRange = []

    for i in input :
        temp = ""

        for j in range(len(i)) :
            if (i[j] == "-") :
                lowRange.append(int(temp))
                temp = ""
            elif (j == len(i)-1) :
                temp += i[j]
                highRange.append(int(temp))
                temp = ""
            else :
                temp += i[j]
    
    return [lowRange, highRange]

# check if ranges overlap
# remove overlaps and subtract lower from higher ones and add together
def uniqueNums(r) :
    # order from lowest low onwards
    orderedLow = [r[0][0]]
    orderedHigh = [r[1][0]]
    for i in range(1,len(r[0])) :
        placed = False
        for j in range(len(orderedLow)) :
            if (r[0][i] < orderedLow[j] and not placed) :
                orderedLow.insert(j,r[0][i])
                orderedHigh.insert(j,r[1][i])
                placed = True
        if(not placed) :
            orderedLow.append(r[0][i])
            orderedHigh.append(r[1][i])
    
    comp = 0
    for i in range(1,len(orderedLow)) :
        if (orderedHigh[i-1-comp]>= orderedLow[i-comp]) :
            del orderedLow[i-comp]
            if (orderedHigh[i-1-comp] < orderedHigh[i-comp]) :
                del orderedHigh[i-1-comp]
            else :
                del orderedHigh[i-comp]
            comp += 1

    num = 0
    for i in range(len(orderedLow)) :
        num += orderedHigh[i]-orderedLow[i]+1
    
    return num

# main portion of the code

f = open("input.txt")
line = f.readline()

ranges = []
fresh = 0

while (line != "\n") :
    ranges.append(line.replace("\n",''))
    line = f.readline()
rangeResult = rangeToArray(ranges)

print(uniqueNums(rangeResult))