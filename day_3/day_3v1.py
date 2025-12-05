# PART 1

# find first matching character, list containing only characters from that onwards 
def bigboi (list, comparison) :
    leftovers = []
    match = False
    for i in comparison :
        for j in list :
            if (i == j and not match) :
                leftovers = list[list.index(j):]
                match = True
    return leftovers

# my precious data
f = open("input.txt")
# line of numbers
bank = f.readline()
sum = 0
# last line of the file is empty
while (bank != "") :
    # go through the bank's batteries (numbers between 1 and 9), searching for the biggest ones
    numChar = ['9','8','7','6','5','4','3','2','1']

    round_1 = bigboi(bank[:len(bank)-2], numChar)
    round_1 += bank[len(bank)-2]

    round_2 = bigboi(round_1[1:], numChar)

    sum += int(round_1[0])*10 + int(round_2[0])

    bank = f.readline()

print(sum)
