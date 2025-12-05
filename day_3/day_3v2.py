# PART 2

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
    left = bank
    joltage = ""

    for i in range(12) :
        left = bigboi(left[:len(left)+(-12+i)], numChar)
        joltage += left[0]
        left += bank[len(bank)+(-12+i):]

        left = left[1:]

    sum += int(joltage)
    bank = f.readline()

print(sum)