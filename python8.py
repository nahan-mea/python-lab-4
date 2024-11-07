def factorial(num):
    """Function to calculate factorial of a number."""
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def sum_series(n):
    """Function to calculate the sum of the series up to the nth term."""
    total_sum = 0
    for i in range(1, n + 1):
        term = (i ** i) / factorial(i)
        total_sum += term
    return total_sum

# Input: number of terms
n = int(input("Enter the number of terms: "))
print("Sum of the series:", sum_series(n))
