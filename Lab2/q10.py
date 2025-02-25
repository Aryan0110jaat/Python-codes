#10. Create a simple calculator
# Function to perform addition 
def add(x, y): 
    return x + y 
 
# Function to perform subtraction 
def subtract(x, y): 
    return x - y 
 
# Function to perform multiplication 
def multiply(x, y): 
    return x * y 
 
# Function to perform division 
def divide(x, y): 
if y != 0: 
return x / y 
else: 
return "Error! Division by zero." 
# Displaying the options to the user 
print("Select operation:") 
print("1. Add") 
print("2. Subtract") 
print("3. Multiply") 
print("4. Divide") 
# Taking user input for the operation 
choice = input("Enter choice (1/2/3/4): ") 
# Taking input for the numbers 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 
# Perform the selected operation 
if choice == '1': 
print(f"{num1} + {num2} = {add(num1, num2)}") 
elif choice == '2': 
print(f"{num1} - {num2} = {subtract(num1, num2)}") 
elif choice == '3': 
print(f"{num1} * {num2} = {multiply(num1, num2)}") 
elif choice == '4': 
print(f"{num1} / {num2} = {divide(num1, num2)}") 
else: 
print("Invalid input!")