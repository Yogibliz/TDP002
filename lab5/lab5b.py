#UPG 5b

data = [
    {'name': 'Jakob', 'position': 'assistant'},
    {'name': 'Åke', 'position': 'assistant'},
    {'name': 'Ola', 'position': 'examiner'},
    {'name': 'Henrik', 'position': 'assistant'}
]

#Search a database in a specified field for a specified value.   
def db_search(db, field, value):
    matches = []

    for match in db:
        if match.get(field) == value:
            matches.append(match)
    return matches

#In this example searching for the field position and the value of examiner.
result = db_search(data, 'position', 'examiner')  #Returns [{'name': 'Ola', 'position': 'examiner'}]

print(result)