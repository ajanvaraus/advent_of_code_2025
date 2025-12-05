# PART 1

# grid of . and @
# if symbol @, check  on index, -1 and +1, on line -1 and +1, b index , -1 and +1
# if at least 4 are . add 1 to result
# if first row add 3 to free spots and don't chec
# if last row add 3 to free sports and don't check b
# if first of the row, add 3 to free spots and don't check left (-1)
# if last of the row, add 3 to free spots and don't check right (+1)

def checkRow(a, c, b, id) :
    around = ""
# check top
    if (a == "") :
       # is it on the right or left side? 
        if (id == 0):
            around = c[id+1]+b[id]+b[id+1]
        elif (id == len(c)-1):
            around = c[id-1]+b[id]+b[id-1]
        else :
            around = c[id-1]+c[id+1]+b[(id-1)]+b[(id)]+b[(id+1)]
# check bottom
    elif (b == "") :
       # is it on the right or left side? 
        if (id == 0):
            around = c[id+1]+a[id]+a[id+1]
            #print(around)
        elif (id == len(c)-1):
            around = c[id-1]+a[id-1]+a[id]
        else :
            around = c[id-1]+c[id+1]+a[id-1]+a[id]+a[id+1]

    else :
        # normal
       # is it on the right or left side? 
        if (id == 0):
            around = c[id+1]+a[id]+a[id+1]+b[id]+b[id+1]
        elif (id == len(c)-1):
            around = c[id-1]+a[id-1]+a[id]+b[id-1]+b[id]
        else :
            around = c[id-1]+c[id+1]+a[id-1]+a[id]+a[id+1]+b[id-1]+b[id]+b[id+1]
    #print(around)
    return checkRoll(around)

def checkRoll(data) :
    roll = 0
    for i in data :
        if (i == '@') :
            roll += 1

    return roll


# main part

# my precious data
f = open("input.txt")
# line of numbers, first 3
row_a = ""
row_c = f.readline().replace('\n','').replace('\t','')
row_b = f.readline().replace('\n','').replace('\t','')

result = 0

# last line of the file is empty
while (row_c != "") :
    # check the entire row, from 0 to length-1
    for i in range(len(row_c)) :
        # 8 around, fewer than 4 can be paper rolls.
        # 4-8 free is acceptable
        if (row_c[i] == '@' and checkRow(row_a,row_c,row_b, i) < 4) :
            result += 1

    # move rows
    row_a = row_c
    row_c = row_b
    row_b = f.readline().replace('\n','').replace('\t','')

print(result)
