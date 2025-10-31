num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))


print("Select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

choice = int(input("Enter your choice(1-4): "))

if choice == 1:
    print(num1,"+",num2,"=", num1+num2)
elif choice == 2:
    print(num1,"-",num2,"=", num1-num2)
elif choice == 3:
    print(num1,"*",num2,"=", num1*num2)
elif choice == 4:
    if num2 != 0:
        print(num1,"/",num2,"=", num1/num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")
    
    
