a = int (input("Enter a number:"))


def cal_fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    print("Factorial of", n, "is", factorial)

cal_fact(a)