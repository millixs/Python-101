# Temperature Convertor Program
# Formula: (Celsius --> Fahrenheit: Celsius_temp * (9/5) + 32)
# Formula: (Fahrenheit --> Celsius: (Fahrenheit_temp - 32) * 5/9)

unit = input("Enter the unit of conversion (c/f): ").strip().lower()

if unit == "c":
    temp = float(input("Enter the temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {temp * (9 / 5) + 32:.2f}°F")

elif unit == "f":
    temp = float(input("Enter the temperature in Fahrenheit: "))
    print(f"Temperature in Celsius: {(temp - 32) * 5 / 9:.2f}°C")

else:
    print("Invalid choice entered")
