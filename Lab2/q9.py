#9. Check whether a number is prime or not.
# Input: Getting a number from the user 
num = int(input("Enter a number: ")) 
 
# Check if the number is less than 2 
if num <= 1: 
    print(f"{num} is not a prime number.") 
else: 
    # Check if the number is divisible by any number from 2 to sqrt(num) 
    is_prime = True 
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0: 
            is_prime = False 
            break 
     
    if is_prime: 
        print(f"{num} is a prime number.") 
    else: 
        print(f"{num} is not a prime number.")