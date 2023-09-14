def replace_vowels_with_dash(input_string):
    
    vowels = "AEIOUaeiou"
    
    result_string = ''.join(['-' if char in vowels else char for char in input_string])
    
    return result_string

input_string = "Hello, World!"
    
modified_string = replace_vowels_with_dash(input_string)
    
print("Modified string: ", modified_string)