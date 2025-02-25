#8. Write a python program to read a number, if it is an even number , print the square of that 
number and if it is odd number print cube of that number
# Input: Getting a number from the user 
num = int(input("Enter a number: ")) 
 
# Checking if the number is even or odd 
if num % 2 == 0: 
    # If the number is even, print the square 
    result = num ** 2 
    print(f"The number is even. The square of {num} is {result}.") 
else: 
    # If the number is odd, print the cube 
    result = num ** 3 
    print(f"The number is odd. The cube of {num} is {result}.")