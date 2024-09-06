#UPG 6c

db = [
('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
]

def insertion_sort(db, func=None):
    for i in range(1, len(db)):
        #Get the current element.
        key = db[i]
        #Index of the element before the current element.
        index_left = i - 1
        #If there are elements to the left of the current element and func(db[index_left]) > func(key) is True keep looping.
        #func(db[index_left]) > func(key) checks if the position to the left is larger than the key.
        while index_left >= 0 and func(db[index_left]) > func(key):
            #If the key is lower value, index_left is moved to the right.
            db[index_left + 1] = db[index_left]
            #Then decrement index_left to keep comparing the positions.
            index_left -= 1
        db[index_left + 1] = key

#Förklaring av while loopen: (Svenska eftersom jag ska kunna förstå lättare om jag kollar tillbaka på det här.)
#while loopen kollar om index_left är mer än eller lika med 0, om det stämmer kommer den även om kolla om func's värde på positionen index_left är större än func's värde på key positionen.
#Om det vänstra värdet skulle vara större så läggs det på 1 för att flytta det till höger. Det skriver då över värdet till höger.
#Sen går index_left värdet ned med 1 för att kunna kolla nästa värde. Men eftersom det börjar på 0, blir det -1 vilket går att den inte kommer förbi while loopen.
#När den inte kommer förbi while loopen, så skriver den ut key på position 0.
#Sen fortsätter den så, och ökar värdet på key för varje runda i for loopen.

#Run the sorting with 'func' lambda e: e[0], which means it will compare the first value in the tuple (the first letter within each pair of parentheses in the list).
sorted = insertion_sort(db, lambda e: e[0])

print(sorted)   #Returns [('@', '.'), ('a', 'u'), ('b', 's'), ('j', 'g'), ('k', 'l'), ('o', 'i'), ('o', 'e'), ('p', 's')]