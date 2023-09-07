import string

def count_characters(input_string):
    
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    punctuation_count = 0
    
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
  
    print("Number of letters in upper case: ", uppercase_count)
    print("Number of lowercase letters: ", lowercase_count)
    print("Number of digits: ", digit_count)
    print("Number of punctuation characters: ", punctuation_count)

input_string = input("Enter the string: ")
count_characters(input_string)