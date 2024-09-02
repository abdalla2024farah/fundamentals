def calculate_factorial(n):
    if n < 0:
        raise ValueError
    
    product = 1
    for num in range(1, n + 1):
        product *= num
    
    return product


n = int(input('Enter a non-negative integer: '))  
result = calculate_factorial(n)  
print(result)  
