#7.  Write a program to print this patterns 
        * 
     *     * 
   *    *     * 
*   *     *     *  
# Number of rows in the pattern 
rows = 4 
 
# Loop for each row 
for i in range(1, rows + 1): 
    # Print leading spaces 
    for j in range(rows - i): 
        print(" ", end="") 
 
    # Print stars with spaces in between 
    for k in range(1, i + 1): 
        print("*", end="   ") 
 
    # Move to the next line after each row 
    print() 