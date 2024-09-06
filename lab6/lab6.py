# #UPG 6a

# def linear_search(db, value, func=None):
#     if func is None:
#         func = lambda x: x
#     for element in db:
#         if func(element) == value:
#             return element
#     return None

# imdb = [
#     {'title': 'The Rock', 'actress': 'Nicholas Cage', 'score': 11},          
#     {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},    
#     {'title': 'Black Hawk Down', 'actress': 'Eric Bana', 'score': 12},
#     ...
# ]

# #Searches the database for the value 10, with a function that tells it to look at 'score' for the value 10.
# search = linear_search(imdb, 10, lambda e: e['score'])
# print(search) #Returns {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}

# #UPG 6b

# def binary_search(db, value, func=None):
#     left = 0
#     right = len(db) - 1
    
#     # Start of a while loop that searches from both left and right ends until they meet in the middle.
#     while left <= right:
#         # Calculate the middle index and retrieve the element at that position.
#         mid = (left + right) // 2
#         element = db[mid]

#         # Check if the condition specified by 'func' is correct for the element at the middle position
#         # and if that element's value is equal to the value we are searching for.
#         if func(element) == value:
#             # If a match is found, return the element.
#             return element
#         #When taking less than on a string it looks at alphabetical order. Ex: Apple < Banana and returns a True or False value.
#         elif func(element) < value:
#             # If the condition is less than the value, continue the search in the right half of the database.
#             left = mid + 1
#         else:
#             # If the condition is greater than the value, continue the search in the left half of the database.
#             right = mid - 1
    
#     # Return None if the search from both ends meets in the middle without finding the value.
#     return None

# people = [{'name': 'Pontus', 'age': 30},
#           {'name': 'Sara', 'age': 20},
#           {'name': 'Xavier', 'age': 19}]

# # Search the 'people' database for 'Pontus' using a function that specifies the search based on the 'name' field.
# bsearch = binary_search(people, 'Pontus', lambda e: e['name'])
# print(bsearch)  # Returns {'name': 'Pontus', 'age': 30}

# # #Example how the less than comparison works with strings.
# # check = 'Apple' < 'Banana'
# # print(check) #Returns True since Apple is alphabetically less than Banana. Because A comes before B
# # check2 = 'Banana' < 'Apple'
# # print(check2) #Returns False since Banana is alphabetically more than Apple. Because B comes after A

# #UPG 6c

# db = [
# ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
# ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
# ]

# def insertion_sort(db, func=None):
#     for i in range(1, len(db)):
#         #Get the current element.
#         key = db[i]
#         #Index of the element before the current element.
#         index_left = i - 1
#         #If there are elements to the left of the current element and func(db[index_left]) > func(key) is True keep looping.
#         #func(db[index_left]) > func(key) checks if the position to the left is larger than the key.
#         while index_left >= 0 and func(db[index_left]) > func(key):
#             #If the key is lower value, index_left is moved to the right.
#             db[index_left + 1] = db[index_left]
#             #Then decrement index_left to keep comparing the positions.
#             index_left -= 1
#         db[index_left + 1] = key

# #Förklaring av while loopen: (Svenska eftersom jag ska kunna förstå lättare om jag kollar tillbaka på det här.)
# #while loopen kollar om index_left är mer än eller lika med 0, om det stämmer kommer den även om kolla om func's värde på positionen index_left är större än func's värde på key positionen.
# #Om det vänstra värdet skulle vara större så läggs det på 1 för att flytta det till höger. Det skriver då över värdet till höger.
# #Sen går index_left värdet ned med 1 för att kunna kolla nästa värde. Men eftersom det börjar på 0, blir det -1 vilket går att den inte kommer förbi while loopen.
# #När den inte kommer förbi while loopen, så skriver den ut key på position 0.
# #Sen fortsätter den så, och ökar värdet på key för varje runda i for loopen.

# #Run the sorting with 'func' lambda e: e[0], which means it will compare the first value in the tuple (the first letter within each pair of parentheses in the list).
# sorted = insertion_sort(db, lambda e: e[0])

# print(sorted)   #Returns [('@', '.'), ('a', 'u'), ('b', 's'), ('j', 'g'), ('k', 'l'), ('o', 'i'), ('o', 'e'), ('p', 's')]

# #UPG 6d

# db = [
#     ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
#     ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
# ]

# def quicksort(db, func):
#     #If the length of the database is less than or equal to 1, return the sorted database.
#     #We need this since the sorting algorithm breaks everything in to parts until it's sorted, which might make on of the lists 1 or less characters long if the other part of the list has more values.
#     #Ex: The right list has more values than the left list, because there is more characters with a higher value than the pivot point then there is characters of a lower values than the pivot points.
#     if len(db) <= 1:
#         return db
    
#     # Choose a pivot point. Select one of two elements if the list is an odd number of elements, otherwise take the middle element.
#     pivot = db[len(db) // 2]
#     # Everything with a lower value goes into the left variable.
#     left = [x for x in db if func(x) < func(pivot)]
#     # Everything with a equal value to the pivot goes into the middle variable.
#     middle = [x for x in db if func(x) == func(pivot)]
#     # Everything with a higher value goes into the right variable.
#     right = [x for x in db if func(x) > func(pivot)]

#     # Sort using the partitioning done earlier. But it's done on each part of the list recursively until everything is in the correct order.
#     # Sort the smaller values first, then add all elements with the same value as the pivot since they don't need further sorting, and finally sort the higher values.
#     return quicksort(left, func) + middle + quicksort(right, func)

# #Variable for the sorted database.
# sorted_db = quicksort(db, lambda e: e[0])

# # Print the sorted database.
# print(sorted_db)

# #UPG 6e

# import os
# import argparse
# copyright_text = ''


# def insert_copyright(destination, copyright_text):
#     # Öppna filen och läs innehållet
#     with open(destination, 'r') as file:
#         file_content = file.read()

#     # Hitta alla förekomster av BEGIN COPYRIGHT 
#     begin_marker = 'BEGIN COPYRIGHT'
#     end_marker = 'END COPYRIGHT'
    
#     #Lists without using the list comprehensions. (Here as an explainer on how list comprehensions work.)
    
#     # begin_positions = []
#     # end_positions = []

#     # for pos, _ in enumerate(file_content):
#     #     if file_content.startswith(begin_marker, pos):
#     #         begin_positions.append(pos)
#     #     if file_content.startswith(end_marker, pos):
#     #         end_positions.append(pos)
    
    
#     #Gets the position of begin copyright and end copyright using enumerate.
#     #If a line starts with begin_marker, the position of that line is added to begin_positions. 
#     #If a line starts with end_marker, the position of that line is added to end_positions. 
#     #These positions will later be used to insert copyright information into the file between the specified markers.
#     begin_positions = [pos for pos, _ in enumerate(file_content) if file_content.startswith(begin_marker, pos)]
#     end_positions = [pos for pos, _ in enumerate(file_content) if file_content.startswith(end_marker, pos)]


#     #Insert copyright information between the markers.
#     #Copy the file_content to a new variable.
#     modified_content = file_content
#     #Pairs upp the start and end positions into a tuple with zip.
#     for begin_pos, end_pos in zip(begin_positions, end_positions):
#         #Assigns the start_index as the position for the begin_marker + the length of the begin_marker so that it remains when adding the copyright information.
#         start_index = begin_pos + len(begin_marker)
#         #Adds the end index as the position for the end_marker since im going to use list splicing.
#         end_index = end_pos
#         #Assigns the modified content from the start to the start index, then the copyright text, then everything from the end index till the end of the file.
#         #The + and - 1 are there to include the '' at the end and start of the respctive marker.
#         modified_content = modified_content[:start_index + 1] + '\n' + copyright_text + '\n' + modified_content[end_index -1:]

#     #Write the modified content to the file.
#     with open(destination, 'w') as file:
#         file.write(modified_content)

# #If the input specifies a directory.
# #Takes a directory, the file extension and a optional new extension.
# def process_directory(directory, file_extension, new_extension=None):
#     #Search for all the files in the root directory (the directory supplied by the user)
#     for root, _, files in os.walk(directory):
#         #Iterate through all the files in the current directory.
#         for file_name in files:
#             #Checks if the file ends with None or the specified file_extension.
#             if file_extension is None or file_name.endswith(file_extension):
#                 #Get the full file path.
#                 destination = os.path.join(root, file_name)
#                 #Then insert copyright in that file.
#                 insert_copyright(destination, copyright_text)
#                 #If a new extension is supplied by the user, add that to the end of the filename.
#                 if new_extension:
#                     #Use os.path.splittext to get the filename then add the new extension in the place of the old one.
#                     new_destination = os.path.splitext(destination)[0] + new_extension
#                     #Then rename the file from the old name + file extension, to the new file name + the new file extension.
#                     os.rename(destination, new_destination)

# def main():
#     parser = argparse.ArgumentParser(description='Infoga copyright-text i filer och kataloger.')
#     parser.add_argument('copyright_file', help='Sökväg till copyright-textfilen')
#     parser.add_argument('destination', help='Sökväg till målet (fil eller katalog)')
#     parser.add_argument('--file_extension', '-c', help='Filtrera filer med filändelse')
#     parser.add_argument('--new_extension', '-u', help='Ny filändelse')
#     args = parser.parse_args()
#     if args.copyright_file:
#         try:
#             with open(args.copyright_file, 'r') as copyright_file:
#                 copyright_text = copyright_file.read()
#         except FileNotFoundError:
#             print(f"Kunde inte hitta filen '{args.copyright_file}'.")
#             return


#     destination = args.destination
#     file_extension = args.file_extension
#     new_extension = args.new_extension

#     if os.path.isfile(destination):
#         insert_copyright(destination, copyright_text)
#         if new_extension:
#             os.rename(destination, os.path.splitext(destination)[0] + "." + new_extension)
#     elif os.path.isdir(destination):
#         process_directory(destination, file_extension, new_extension, copyright_text)
#     else:
#         print('Målet finns inte eller är varken en fil eller katalog.')

# if __name__ == '__main__':
#     main()