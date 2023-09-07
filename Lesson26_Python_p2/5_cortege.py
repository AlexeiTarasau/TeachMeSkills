def are_elements_unique(input_tuple):
    
    unique_set = set(input_tuple)
    return len(unique_set) == len(input_tuple)

input_tuple = (1, 2, 5, 4, 5)

result = are_elements_unique(input_tuple)
    
if result:
    print("All elements of a tuple are unique.")
else:
    print("There are duplicates in the cortege.")
