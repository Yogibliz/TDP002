# UPG 5h

def compose(F_a, F_b):
    def F_res(x):
        return F_a(F_b(x))
    return F_res

def partial(func, value):
    return lambda *args: func(value, *args)

# Create a filter function using partial
# Uses the built in filter function on the filter_func provided.
# The built in filter function takes a function which retruns a True or False value, and an iterable, in this case range(10).
def create_filter(filter_func):
    return partial(filter, filter_func)

# Create a map function using partial
# Uses the built in map function on the map_func provided.
# The built in map function takes a function which modiefies the value of an iterable, then returns that value, in this case squares all the number in range(10).
def create_map(map_func):
    return partial(map, map_func)

#Takes two functions as arguments, filter_func and map_func.
#Returns a new function, composed_func, which merges the two functions into one which both filters and maps.  
#Composed_funcs is a function created by composing the create_map and create_filter functionalities into one with the compose function.
#Then a new function is added which takes an input list, in this case range(10).
#Then returns a list of all those numbers after passing through the composed_funcs function. Then returns that list as map_and_filter.
def make_filter_map(filter_func, map_func):

    #Compose runs the 2nd func first, which is why filter func is there.
    #This way it filters then maps.
    composed_funcs = compose(create_map(map_func), create_filter(filter_func))
    
    #Takes the input list then returns the list after it's been run through the filter and map functions.
    def map_and_filter(input_list):
        return list(composed_funcs(input_list))
    return map_and_filter

#Filter_func is the first lambda function, which removes all the even numbers.
#Map_func is the second lambda function, which squares the numbers that are left.
process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)
#Inputs all the numbers (1-9) and runs them through the filter and map.
result = process(range(10))
print(result)  # Output: [1, 9, 25, 49, 81]