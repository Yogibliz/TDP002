height = int(input("How tall do you want the table to be?: "))

width = int(input("How wide do you want the table to be?: "))

for y in range(1, height + 1):  
    #Loops through the numbers from 1 to the input number. +1 to count the number that was input aswell.
    for x in range(1, width + 1): 
        z = y * x   #Calculates the multiplication table.
        print(z, end="\t")  #Prints out the rows from the for loops for height and width Using \t to space everything and make sure it stays on the same row.
    print() #Prints out an empty line and loops it back for the next row.