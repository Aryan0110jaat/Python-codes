#7. Write a python program to read radius of a circle and print the area 
 
# Input: Getting the radius of the circle from the user 
radius = float(input("Enter the radius of the circle: ")) 
 
# Calculating the area of the circle using the formula: area = π * radius^2 
area = math.pi * radius ** 2 
 
# Output: Displaying the area 
print(f"The area of the circle with radius {radius} is: {area:.2f}") 