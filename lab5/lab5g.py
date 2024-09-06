# UPG 5g

#Adds two functions together. 
#By taking the input number into the 2nd function then adding it together with the first function.
#Ex: compose(multiply_five, add_ten(x)) change x by example 3, then the output will be 65, because 3+10 = 13, then 13*5 = 65. 
def compose(F_a, F_b):
    def F_res(x):
        return F_a(F_b(x))
    return F_res

#Multiplies the number of choice by 5.
def multiply_five(n):
    return n * 5

#Adds 10 to the number of choice.
def add_ten(n):
    return n + 10

#Counts the second variable firts, then adds the first variable to the value. ((10 + 3) * 5)
composition = compose(multiply_five, add_ten)
result = composition(3)
print(result)  # Output: 65

#Counts the second variable firts, then adds the first variable to the value. ((3 * 5) + 10)
another_composition = compose(add_ten, multiply_five)
result = another_composition(3)
print(result)  # Output: 25