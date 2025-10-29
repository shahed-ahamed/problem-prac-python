def fact(n):
    return 1 if n==0 else n*fact(n-1)

num = int(input("Enter a number: "))
print("Factorial:", fact(num))
