#4. Write a python program to read three numbers and if any two variables are equal, print that number
# Input: Getting three numbers from the user 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
num3 = float(input("Enter the third number: ")) 
# Checking if any two numbers are equal and printing that number 
if num1 == num2: 
print(f"The common number is: {num1}") 
elif num1 == num3: 
print(f"The common number is: {num1}") 
elif num2 == num3: 
print(f"The common number is: {num2}") 
else: 
print("No two numbers are equal.")