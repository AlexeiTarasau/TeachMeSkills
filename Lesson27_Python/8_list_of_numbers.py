def find_median(numbers):
   
    sorted_numbers = sorted(numbers)
   
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[n // 2]
    
    return median

numbers = [5, 2, 9, 1, 5, 6]
    
median = find_median(numbers)
    
print("List median: ", int(median))