def sort_descending(numbers):
    
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

input_numbers = [5, 2, 9, 1, 5, 6]
    
descending_numbers = sort_descending(input_numbers)
    
print("Array in descending order: ", descending_numbers)