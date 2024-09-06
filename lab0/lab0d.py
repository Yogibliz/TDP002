# UPG 1d

# https://www.tutorialspoint.com/How-to-perform-square-root-without-using-math-module-in-Python

prime_sum = 0   #A variable to assign the result to.

for num in range(2, 1001):  #Loops through the range 2-1000, skipping 1 since you can't take the square root out of 1.
    is_prime = True #Boolean to make sure if something is a prime number or not.
    for sum in range(2, int(num**1/2) + 1):   #Loops through range of 2 - square root of sum and adds 1 to make sure it goes check the square root itself. (Example: If we examine the number 16, the square root would be 4. If we didn't include +1, python would only loop until 3 and miss that 16 is actually divisible by 4)
        if num % sum == 0:    #Checks if the sum is devisive with i without any rest product
            is_prime = False
            break   #Breaks out of the loop and tries another number if the number was not a prime number.
    if is_prime:
        prime_sum += num    #Adds up all the prime numbers into the prime_sum variable

print(f"Summan av alla primtal under 1000 är {prime_sum}.") #Prints out the prime sum