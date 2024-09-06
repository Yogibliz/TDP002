valuelist = []  #Empty list to append the values into for comparison.

for i in range(3):  #Loops three times to get user inputs for the comparison.
    while True:
        try:
            value = int(input(f"Skriv in värde {i + 1}: ")) #Asks the user for an integer input, prints the current value to be entered using i + 1 to make sure it doesn't start counting from 0.
            valuelist.append(value) #Adds the user input into the list, if it meets the requirment (being an integer)
            break
        except ValueError:
            print("Det verkar inte vara rätt, försök igen. (Ange ett heltal)")  #In case there was an input that was not of an integer type, prints out and error and allows the user to try again
            continue

#highest_value = max(valuelist)  #Find the highest balue in the list, can't use for this though
highest_value = valuelist[0]    #Start value at the 1st input in the list
for x in valuelist:
    if x > highest_value:   #Controls the values in the list, if bigger than x keep going
        highest_value = x   #If the value from the list was of a higher value, stick that value onto the highest_value variable


print(f"Det högsta värdet är: {highest_value}")