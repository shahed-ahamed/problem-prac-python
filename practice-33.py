temp = float(input("Enter temperature in Celsius: "))

print("Choose the conversion you want to perform:")
print("1. Fahrenheit")
print("2. Kelvin")

choice = int(input("Enter choice (1 or 2): "))

if choice == 1:
    fahrenheit = (temp * 9/5) + 32
    print(f"{fahrenheit}°F is the Fahrenheit equivalent of {temp}°C.")
    
elif choice == 2:
    kelvin = temp + 273.15
    print(f"{kelvin}K is the Kelvin equivalent of {temp}°C.")
    
else:
    print("Invalid choice. Please enter 1 or 2.")


