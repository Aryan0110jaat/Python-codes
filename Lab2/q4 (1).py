#4.  Write a program to check whether a character is vowel or 
consonants. 
# Input: Getting a character from the user 
char = input("Enter a character: ").lower()  # Convert to lowercase for easy comparison 
 
# Checking if the character is a vowel or consonant 
if char in 'aeiou': 
    print(f"{char} is a vowel.") 
elif char.isalpha():  # Check if the character is a letter 
    print(f"{char} is a consonant.") 
else: 
    print("Please enter a valid alphabetic character.")