#5. Write a program to find the smallest of two numbers.
#Input: Getting two numbers from the user 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
 
# Finding the smallest number 
if num1 < num2: 
    print(f"The smallest number is {num1}.") 
elif num2 < num1: 
    print(f"The smallest number is {num2}.") 
else: 
    print("Both numbers are equal.") 