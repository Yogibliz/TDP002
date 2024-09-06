# UPG 1b

sum = 1   #Start sum of 1, since 0 has no value and thus is not a positiv integer that can be multiplied.

for i in range(1, 513):   #Loop for every positive integer in the range 1-512  
    sum = sum * i #Multiplies the sum and the positiv integer for the entire loop range and adds them together into the sum variable
    print(sum)    #Prints the new sum after every loop.