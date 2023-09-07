def common_characters(str1, str2):
   
    set1 = set(str1)
    set2 = set(str2)
    
    common_set = set1.intersection(set2)
        
    print("Characters appearing on both lines: ")
    for char in common_set:
        print(char)

str1 = "abcdef"
str2 = "defghij"
    
common_characters(str1, str2)
