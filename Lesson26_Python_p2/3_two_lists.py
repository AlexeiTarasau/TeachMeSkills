def common_elements(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    
    common_set = set1.intersection(set2)
    
    print("Elements present in both lists: ")
    for element in common_set:
        print(element)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
    
common_elements(list1, list2)
