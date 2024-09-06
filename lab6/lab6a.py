#UPG 6a

def linear_search(db, value, func=None):
    if func is None:
        func = lambda x: x
    for element in db:
        if func(element) == value:
            return element
    return None

imdb = [
    {'title': 'The Rock', 'actress': 'Nicholas Cage', 'score': 11},          
    {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},    
    {'title': 'Black Hawk Down', 'actress': 'Eric Bana', 'score': 12},
    ...
]

#Searches the database for the value 10, with a function that tells it to look at 'score' for the value 10.
search = linear_search(imdb, 10, lambda e: e['score'])
print(search) #Returns {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}