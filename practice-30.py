n = int(input("Enter the prime number: "))

is_prime = True

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break   
    else:
        is_prime = True
        
if is_prime and n > 1:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
