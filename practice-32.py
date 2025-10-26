decimal = int(input("Enter a decimal number: "))

print("Which conversion do you want to perform?")
print("1. Binary")
print("2. Octal")
print("3. Hexadecimal")
choice = int(input("Enter your choice (1 or 2 or 3): "))
if choice == 1:
    binary = bin(decimal)
    print(f"{binary} is the binary representation of {decimal}.")

elif choice == 2:
    octal = oct(decimal)
    print(f"{octal} is the octal representation of {decimal}.")
    
elif choice == 3:
    hexadecimal = hex(decimal)
    print(f"{hexadecimal} is the hexadecimal representation of {decimal}.")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
