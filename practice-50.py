#recursion use kore n songkhar first natural number er sum ber kora

a=int(input("Enter a number: "))

def sum_n(n):
    if n==0:
        return 
    else:
        return n+sum_n(n-1)
    
print(f"Sum of first {a} natural number is: ", sum_n(a))

sum_n(a)


