#5. Write a python program to read three numbers and find the smallest among them 
# Input: Getting three numbers from the user 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
num3 = float(input("Enter the third number: ")) 
 
# Finding the smallest number 
smallest = num1 
 
if num2 < smallest: 
    smallest = num2 
if num3 < smallest: 
    smallest = num3 
 
# Output: Displaying the smallest number 
print("The smallest number among", num1, ",", num2, "and", num3, "is:", smallest) 