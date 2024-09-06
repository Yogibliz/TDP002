# UPG 5f

#Take a function and value, adds those into a lambda function which returns the value of *args after being affected by the function.
#Ex: partial(add, 5) where the add func is x + y, and the user inputs one of them as 3, then partial would be (3 + 5).
def partial(func, value):
    return lambda *args: func(value, *args)

#Adds two numbers together.
def add(x, y):
    return x + y

#Adds five to the number selected.
add_five = partial(add, 5)

#Adds five to the input value of 3.
result1 = add_five(3)
print(result1) # Output: 8

#Adds five to the input value of 16.
result2 = add_five(16)
print(result2) # Output: 21