# Weight Converter Program
# Formula: (Pounds --> Kilograms: weight_in_pounds * 0.45359237)
# Formula: (Kilograms --> Pounds: weight_in_kilograms * 2.2)

response = input("Enter 1 to convert lbs ➝ kg, or 2 to convert kg ➝ lbs: ").strip()

if response == "1":
    weight_lbs = float(input("Enter your weight in pounds(lbs): ").strip())
    weight = weight_lbs / 2.205
    print(f"The converted weight in kilograms(kg) is: {weight:.2f}kg")

elif response == "2":
    weight_kg = float(input("Enter your weight in kilograms(kg): ").strip())
    weight = weight_kg * 2.205
    print(f"The converted weight in pounds(lbs) is: {weight:.2f}lbs")

else:
    print("Invalid choice entered")
