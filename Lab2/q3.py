#3.  Check whether an entered year is leap year or not.
# Input: Getting a year from the user 
year = int(input("Enter a year: ")) 
# Checking if the year is a leap year 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
print(f"{year} is a leap year.") 
else: 
print(f"{year} is not a leap year.")