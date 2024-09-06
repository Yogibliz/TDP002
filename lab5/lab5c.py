#UPG 5c

#Returns true if the input word is in the list and false if it isn't.
def contains(element, list_data):
    for item in list_data:
        if element == item:
            return True
    return False

#The list_data (getting a list of words, by splitting a sentence.)
haystack = 'Can you find the needle in this haystack?'.split()

print(contains('find', haystack))    # True since find is split by a space
print(contains('needle', haystack))  # True since needle is split by a space
print(contains('haystack', haystack)) # False since haystack has a ? at the end