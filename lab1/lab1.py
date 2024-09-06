import datetime

date = datetime.datetime.now()

name = input("Vad heter du?: ")
print(f"Hej {name}!")
age = date.year - int(input("Mata in din ålder: "))
print(f"Du föddes år {age}.")
birth_place = input("Vilket län föddes du i: ")
print(birth_place)

#Splits the first half of the name input and the second half of the birth_place input and adds them together.
half_half = name[:len(name) // 2] + birth_place[len(birth_place) // 2:]

print(f"Första halvan av ditt namn och andra halvan av ditt län är: \n{half_half}")