# PART 2
# sadly the data has to be copied from og_input.txt to input.txt every time you want to produce the needed result but idc it works
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

keepGoing = True
result = 0


while (keepGoing) :
    # my precious data
    f = open("input.txt")
    # line of numbers, first 3
    row_a = ""
    row_c = f.readline().replace('\n','')
    row_b = f.readline().replace('\n','')
    temp_c = row_c

    roundResult = 0
    update = ""
# last line of the file is empty
    while (row_c != "") :
        # check the entire row, from 0 to length-1
        for i in range(len(row_c)) :
            # 8 around, fewer than 4 can be paper rolls.
            # 4-8 free is acceptable
            if (row_c[i] == '@' and checkRow(row_a,row_c,row_b, i) < 4) :
                roundResult += 1
                temp_c = temp_c[:i]+'.'+temp_c[i+1:]
                print(temp_c)
        update += temp_c + "\n"

        # move rows
        row_a = row_c
        row_c = row_b
        row_b = f.readline().replace('\n','')

        temp_c = row_c
    f.close()
    f = open("input.txt", 'w')
    f.write(update)
    f.close()
    result += roundResult
    if (roundResult == 0) :
        keepGoing = False



print(result)
