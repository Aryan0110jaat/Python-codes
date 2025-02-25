#1. Write a python program to swap two numbers using a third variable 
# Input: Getting two numbers from the user 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
# Swapping using a third variable 
temp = num1 
num1 = num2 
num2 = temp 
# Output: Displaying the swapped numbers 
print("After swapping:") 
print("First number:", num1) 
print("Second number:", num2)