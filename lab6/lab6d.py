#UPG 6d

db = [
    ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
    ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
]

def quicksort(db, func=lambda x:x):
    #If the length of the database is less than or equal to 1, return the sorted database.
    #We need this since the sorting algorithm breaks everything in to parts until it's sorted, which might make on of the lists 1 or less characters long if the other part of the list has more values.
    #Ex: The right list has more values than the left list, because there is more characters with a higher value than the pivot point then there is characters of a lower values than the pivot points.
    if len(db) <= 1:
        return db
    
    # Choose a pivot point. Select one of two elements if the list is an odd number of elements, otherwise take the middle element.
    pivot = db[len(db) // 2]
    # Everything with a lower value goes into the left variable.
    left = [x for x in db if func(x) < func(pivot)]
    # Everything with a equal value to the pivot goes into the middle variable.
    middle = [x for x in db if func(x) == func(pivot)]
    # Everything with a higher value goes into the right variable.
    right = [x for x in db if func(x) > func(pivot)]

    # Sort using the partitioning done earlier. But it's done on each part of the list recursively until everything is in the correct order.
    # Sort the smaller values first, then add all elements with the same value as the pivot since they don't need further sorting, and finally sort the higher values.
    return quicksort(left, func) + middle + quicksort(right, func)

#FIX Return the quicksort result to starting db so the print works as expected. ????

# Print the sorted database.
print(quicksort(db, lambda e: e[0]))

'BEGIN COPYRIGHT'

'END COPYRIGHT'