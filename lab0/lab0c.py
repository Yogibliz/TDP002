# UPG 1c

def smallest_devisive():
    
    sum = 1   #Start sum of 1, since 0 can't be devided.

    while True:   #While loop that runs until the number is found
        delbart = True    #Checks if everything is devisive in the range.
        for i in range(1, 14):
            if sum % i != 0:  #Checks if the sum is not evenly devisive with % i (1-13).
                delbart = False
                break
        if delbart:   #Returns sum if a number is evenly devisable by 1-13.
            return sum
        elif delbart == False:  #Adds 1 to the sum and tests the next number if the number couldn't be devided evenly with everything 1-13.
            sum += 1

result = smallest_devisive() #Assigns the results of the smallest_devisive function to a variable which is printed.
print(result)