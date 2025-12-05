# PART 1

# ranges into array
# ingredients into array
# if ingredient is in a range +1 to fresh

# isFresh function
# gets an ingredient integer and range array
# return true/false
def isFresh (ingredient, r) :
    match = False

    for i in range(len(r[0])) :
        if (r[0][i] <= ingredient and r[1][i] >= ingredient) :
            match = True
    
    return match

# rangeToArray function
# gets array of ranges ["1-4","2-6",...]
# return array of tuples [[low, high], [low, high],...]
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

# main
# while loop until ""

# get input until "\n", first append into ranges array
# then get input until "\n", append into ingredients array

# check freshness
# add fresh ingredients to total
# print total
f = open("input.txt")
line = f.readline()

ranges = []
ingredients = []
fresh = 0

while (line != "\n") :
    ranges.append(line.replace("\n",''))
    line = f.readline()
rangeResult = rangeToArray(ranges)

line = f.readline()

while (line != "") :
    ingredients.append(int(line.replace("\n",'')))
    line = f.readline()

for i in ingredients :
    if (isFresh(i, rangeResult)) :
        fresh += 1

print(fresh)