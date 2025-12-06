# PART 1

# global file r
r = open("read.txt")

#file handler
def handler() :
    # send updated file for a new round until everything has been read

    # input to read file
    x = open("read.txt", "w")
    for i in open("input.txt") :
        x.write(i)
    x.close()

    result = 0
    stop = False
    
    while (not stop) :
        # call for column handler
        op, temp, stop = looper()
        result += temp

        # update files
        r = open("read.txt", "a")
        w = open("write.txt")
        for i in w :
            r.write(i)
        w.close()
        w = open("write.txt", "w")
        w.truncate(0)
        r.close()
        r = open("read.txt")

    return result

# recursive handler for one column
# writes trimmed lines into t1
def looper() :
    operation = ""
    result = 0
    stop = False
    line = r.readline()
    print(line)
    # test print
    if (12 == int(line)) :
        stop = True
    # test write
    x = open("write.txt", "w")
    x.write(str(int(line)+1))
    x.close()
    return [operation, result, stop]

def main() :
    # hopefully just function call and result print
    result = handler()
    print(result)

main()