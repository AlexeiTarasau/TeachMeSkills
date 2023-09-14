def find_common_and_unique_elements(list1, list2):
    
    common_elements = list(set(list1).intersection(set(list2)))
   
    unique_elements = list(set(list1 + list2) - set(common_elements))
    
    return unique_elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
    
result = find_common_and_unique_elements(list1, list2)

print("Unique elements: ", result)