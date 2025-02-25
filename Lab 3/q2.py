#2. Write a python program to swap two numbers without using third variable
# Input: Getting two numbers from the user 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
# Swapping without using a third variable 
num1 = num1 + num2 
num2 = num1 - num2 
num1 = num1 - num2 
# Output: Displaying the swapped numbers 
print("After swapping:") 
print("First number:", num1) 
print("Second number:", num2)