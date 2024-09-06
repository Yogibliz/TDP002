# UPG 2 bild 1

# def main():
#     numbers = [1, 2, 3] #Lista med nummer
#     numbers_reference = numbers #En referens till listan
#     return numbers_reference    #Returnera värdet av listan.

# result = main()
# print(result)

# #UPG 2 bild 2

# def main():
#     numbers = [1, 2, 3]
#     numbers_reference = list(numbers)
#     return numbers_reference

# result = main()
# print(result)

# #UPG 2 bild 3

# def add_element(l, e):
#     l.append(e)

# def main():
#     numbers = [1, 2, 3]
#     add_element(numbers, 4)
#     return numbers

# result = main()
# print(result)

# #UPG 2 bild 4

# def add_element(l, e):
#     l.append(e) #Appends the element to the list
#     return l

# def main():
#     numbers = [1, 2, 3]
#     new_numbers = add_element(numbers[:], 4)
#     return numbers, new_numbers

# result = main()
# print(result)

# UPG 2a del 1

# def ASCII():
#     print("*" * (len(string) + 4))  #+4 Since frame() prints out "* + space" and "space + *" before and after the string.

# def frame(s):
#     print("* " + s + " *")

# string = str(input("Skriv en sträng: "))
# ASCII()
# frame(string)
# ASCII()

# #UPG 2a del 2

# def triangle(x):
#     for i in range(x):  #Loops the amounts of time the user inputs into height.
#         for j in range(i + 1):  #Prints out the same amount of stars + 1 since python excludes the last number.
#             print("* ", end="")
#         print("")   #Empty line after each run to make sure it builds the shape correctly.

# height = int(input("Skriv höjd på triangeln: "))
# triangle(height)

# UPG 2a del 3

# def flag(x):
#     for i in range(x * 8):
#         half_height = (x * 8 // 2)
#         half_length = (x * 21 // 2)
#         print("*" * half_length, end="")
#         print(" ", end="")
#         print("*" * half_length, end="\n")
#         if i == half_height - 1:    #-1 Because the first line has the index 0.
#             print()

# flag_length = int(input("How long do you want the flag (Multiplies with 21): "))
# flag(flag_length)

# #UPG 2b

# slist = "shopping_list.txt"

# def menu():
#     while True:
#         user_choice = input("1. Show the shopping list\n2. Add to the shopping list\n3. Remove from the shopping list\n4. Edit the shopping list\nExit the program (e or q)\nWhat do you want to do?: ")
#         print() #Empty line ahead of the output
#         if user_choice == 1:
#             shopping_list(slist)
#         elif user_choice == 2:
#             user_add = str(input("What do you want to add to the list?: "))
#             shopping_add(slist, (user_add + "\n"))
#         elif user_choice == 3:
#             shopping_remove(slist)
#         elif user_choice == 4:
#             shopping_edit(slist)
#         elif user_choice == "e" or "q":
#             print("Bye!")
#             break
#         else:
#             print("Error, wrong input, try again.")

# def create_shopping_list(): #Creates the shopping list if it doesn't exist already
#     try:
#         with open(slist, "x") as f:
#             pass
#     except FileExistsError:
#         pass

# def shopping_list(f):
#     create_shopping_list()
#     with open(f) as file:    #Opens the file
#         for i, line in enumerate(file, 1):   #Index the lines in the file, i is the index number and line is the line content
#             print(f"{i}: {line}", end="")   #End="" to make sure it doesn't make a blank line between the items when printing out the list
#         print("\n") #Prints an empty row after the list has been shown to the user

# def shopping_add(f, a):
#     create_shopping_list()

#     file = open(f, "a")
#     file.write(a)
#     file.close()

# def shopping_remove(f):
#     create_shopping_list()

#     shopping_list(slist) #Displays the current list with their indexes
#     line_remove = int(input("Which line do you want to remove?: "))
#     with open(f, "r") as file:  #Opens the file in read mode and assigns the lines a index
#         lines = file.readlines()
#     if 1 <= line_remove <= len(lines):   #Checks the input, makes sure the input is more than 1 and less or equal to the length of the list
#         lines.pop(line_remove - 1)  #Removes the line from the index the user entered -1 since the list starts from 1 instead of 0
#         with open(f, "w") as file:  #Opens the file in write mode, to allow the lines.pop modified version to be writen into the file
#             file.writelines(lines)  #Writes the modified version of "lines" into the file to overwrite the current version

# def shopping_edit(f):
#     create_shopping_list()

#     shopping_list(f)
#     edit_line = int(input("Which line do you want to edit?: "))
#     with open(f, "r") as file:  #Opens the file in read mode
#         lines = file.readlines()
#     if 1 <= edit_line <= len(lines):    #Checks if the input is a valid index that is present in the file
#         line_content = lines[edit_line - 1].strip() #Gets the content out of the line, while stripping it of whitespace and newline characters that might be present
#         new_content = input(f"What do you want to replace {line_content} with?: ")  #Asks the user what it wants to replace the old content of the line with
#         lines[edit_line - 1] = new_content + "\n"   #Updates the file at the line that was selected with the content that the user was asked to input, then adds a newline character
#         with open(f, "w") as file:  #Opens the file in write mode
#             file.writelines(lines)  #Writes the modified version of the selected line to shopping list

# menu()