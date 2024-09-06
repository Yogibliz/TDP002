valuelist = []


while True:
    List_choice = input("Vilken typ av lista vill du ha? (E: Exakt Lista | R: Läsbar Lista): ")
    if List_choice in ["E", "e", "R", "r"]:
        break
    else:
        print("\nTry again, you can enter (E/e) or (R/r)\n")



for i in range(2):  #Loops 2 times to get user inputs for the comparison.
    while True:
        print("Värde 1: Lånesumma | Värde 2: Ränta\n")
        value = int(input(f"Skriv in värde {i + 1}: ")) #Asks the user for an integer input, prints the current value to be entered using i + 1 to make sure it doesn't start counting from 0.
        if value in range(1, 101):
            valuelist.append(value) #Adds the user input into the list, if it meets the requirment (being an integer)
            break
        else:
            print("Det ser inte rätt ut, försök igen. (Ange ett heltal mellan 1-100)\n")  #In case there was an input that was not of an integer type, prints out and error and allows the user to try again
            continue

if List_choice in ["E", "e"]:

    print("-------Lånöversikt-------")

    for _ in range(1, 13):
        print(f"{_} | {valuelist[0]} kr | {valuelist[1]}% Ränta")   #Prints the Exact number
        valuelist[0] += valuelist[0] * (valuelist[1] / 100)

elif List_choice in ["R", "r"]:
    
    print("-------Lånöversikt-------")

    for _ in range(1, 13):
        print(f"{_} | {round(valuelist[0])} kr | {valuelist[1]}% Ränta")   #Prints the numbers rounded to make the list more readable
        valuelist[0] += valuelist[0] * (valuelist[1] / 100)

else:
    print("This was not supposed to happen :/")