num = int(input("Enter a number you want to sum up to: "))

def sum_natural_numbers(n):
    if n < 1:
        return 0
    return n + sum_natural_numbers(n - 1)
result = sum_natural_numbers(num)
print(f"The sum of the first {num} natural numbers is: {result}")

