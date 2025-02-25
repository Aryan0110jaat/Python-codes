#6.  Find the Factorial of a Number 
# Input: Getting a number from the user 
num = int(input("Enter a number to find its factorial: ")) 
 
# Checking if the number is non-negative 
if num < 0: 
    print("Factorial is not defined for negative numbers.") 
else: 
    # Calculating factorial using a loop 
    factorial = 1 
    for i in range(1, num + 1): 
        factorial *= i 
     
    # Output: Displaying the factorial 
    print(f"The factorial of {num} is {factorial}.") 