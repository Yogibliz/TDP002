# UPG 5e

#Generates the list by taking the number +1 and appending to the empty list 'result'. Then returns the filled list.
def generate_list(func, n):
    result = []
    for i in range(1, n+1):
        result.append(func(i))
    return result

#Returns the number that is selected.
def mirror(x):
    return x
#Returns the star character times the number selected.
def stars(n):
    return '*' * n

#Returns a list of the numbers from 1 to 4.
result1 = generate_list(mirror, 4)
print(result1)  # Output: [1, 2, 3, 4]

#Returns a list of stars in the amounts from 1 to 5.
result2 = generate_list(stars, 5)
print(result2)  # Output: ['*', '**', '***', '****', '*****']