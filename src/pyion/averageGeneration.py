def calculateAverage(input):
    #check if the input list has a length that is divisible by 3
    if len(input)%3 != 0:
            return None

    sublists = [input[n:n+3] for n in range(0, len(input), 3)]  # sublists contains sublists of length 3, subList is in the format of [[a,b,c],[c,d,e]...]
    #total = 0   #this is the total/sum of a block of three

    averagelist = [] #this is the list that holds all the calculated average

    #head = ["Average Voltage"] #this is the header for the table that stores average value

    for item in sublists: # every item is a sublist in the format of [x,y,z]
        total = 0
        for i in item:  #every i is a number in sublist, like x in [x,y,z]
                total = total + i   # calculate the total of a sublist like [x,y,z]
        average = total/3 #for every item/sublist of three elements, calculate the average
        averagelist.append(average)#store the average of a sublist in a table

    #now make a table from filled-up averagelist and return it
    #return tabulate(averagelist,headers=head, tablefmt="grid")
    return averagelist