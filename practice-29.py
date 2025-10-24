a=0
b=1

n = int(input("Enter the number of terms: "))
print (a,b, end =" ")
for _ in range(n):
    c=a+b
    print(c, end =" ")
    a=b
    b=c
