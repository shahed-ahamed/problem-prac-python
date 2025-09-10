# Even and Odd numer check

number = int(input("Enter a number: "))

rem= number % 2

if (rem == 0):
    print ("Even Number")
else:
    print ("Odd Number")




    # Greated of three numbers by user given input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if ( a>b and a>c):
    print (a, "is greatest")
elif (b>c and b>a):
    print (b, "is greatest")
else:
    print (c, "is greatest")

    #check a number that is multiple of 7 

num = int(input("Enter a number: "))

rem = num % 7

if (rem == 0):
    print (num, "is multiple of 7")
else:
    print (num, "is not multiple of 7")