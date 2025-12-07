# PART 1

#file handler
def handler() :
    data = []
    for i in open("input.txt") :
        data.append(i)

    result = 0
    stop = False
    
    while (not stop) :
        # getting the data into a variable
        piece = []
        for i in range(len(data)) :
            part, space, line = data[i].partition(" ")
            data[i] = line.strip()
            piece.append(part)

        # call for column handler
        op, temp, = looper(piece)
        result += temp

        # end condition
        if (data[0] == "") :
            stop = True

    return result

# recursive handler for columns
def looper(data) :

    operation = ""
    result = 0

    if (data[0] == "+") :
        operation = data[0]
    elif (data[0] == "*") :    
        operation = data[0]
        result = 1
        
    elif (data[0].isnumeric()):
        operation, result = looper(data[1:])
        
        if (operation == "+") :
            result += int(data[0])
        elif (operation == "*") :
            result = result * int(data[0])
            print(data[0])
            print(result)
    return [operation, result]

def main() :
    # hopefully just function call and result print
    result = handler()
    print(result)

main()