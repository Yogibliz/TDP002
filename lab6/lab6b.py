#UPG 6b

def binary_search(db, value, func=lambda x:x):
    left = 0
    right = len(db) - 1
    
    # Start of a while loop that searches from both left and right ends until they meet in the middle.
    while left <= right:
        # Calculate the middle index and retrieve the element at that position.
        mid = (left + right) // 2
        element = db[mid]

        # Check if the condition specified by 'func' is correct for the element at the middle position
        # and if that element's value is equal to the value we are searching for.
        if func(element) == value:
            # If a match is found, return the element.
            return element
        #When taking less than on a string it looks at alphabetical order. Ex: Apple < Banana and returns a True or False value.
        elif func(element) < value:
            # If the condition is less than the value, continue the search in the right half of the database.
            left = mid + 1
        else:
            # If the condition is greater than the value, continue the search in the left half of the database.
            right = mid - 1
    
    # Return None if the search from both ends meets in the middle without finding the value.
    return None

people = [{'name': 'Pontus', 'age': 30},
          {'name': 'Sara', 'age': 20},
          {'name': 'Xavier', 'age': 19}]

# Search the 'people' database for 'Pontus' using a function that specifies the search based on the 'name' field.
bsearch = binary_search(people, 'Pontus')
print(bsearch)  # Returns {'name': 'Pontus', 'age': 30}

# #Example how the less than comparison works with strings.
# check = 'Apple' < 'Banana'
# print(check) #Returns True since Apple is alphabetically less than Banana. Because A comes before B
# check2 = 'Banana' < 'Apple'
# print(check2) #Returns False since Banana is alphabetically more than Apple. Because B comes after A