def multiply_numbers(a, b):
    result = a * b
    return result

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
result = multiply_numbers(num1, num2)
print(f"The result of multiplying {num1} by {num2} is equal to {result}")