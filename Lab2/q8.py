#8. Write a program to print this series1 1 2 3 5 8 13
# Initial values for the Fibonacci sequence 
a, b = 1, 1 
 
# Number of terms to print in the series 
n = 7 
 
# Printing the series 
print(a, end=" ") 
for _ in range(1, n): 
    print(b, end=" ") 
    a, b = b, a + b 
