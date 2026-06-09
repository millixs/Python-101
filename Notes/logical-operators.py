# Logical Operators: Used to evaluate multiple conditions
# or = at least one condition must be true
# and = both conditions must be true
# not = inverts the condition (not False → True, not True → False)

# Weather Assistant Program
print("🌦️ Welcome to the Weather Assistant")

temp = float(input("Enter the current temperature: "))
is_sunny = input("Is it sunny? (yes/no): ").strip().lower() == "yes"
is_raining = input("Is it raining? (yes/no): ").strip().lower() == "yes"

# Determine event cancellation
if temp >= 45 or temp <= 0 or is_raining:
    print("The outdoor event is CANCELLED 🚨")
else:
    print("The outdoor event is STILL SCHEDULED ✅")

# Weather description
if is_sunny and not is_raining:
    if temp >= 30:
        print("It's HOT and SUNNY 🔥")
    elif temp <= 0:
        print("It's COLD and SUNNY ❄️")
    else:
        print("It's WARM and SUNNY 🌤️")
elif not is_sunny and is_raining:
    print("It's RAINY and CLOUDY 🌧️")
elif not is_sunny and not is_raining:
    print("It's CLOUDY ☁️")
else:
    print("The weather conditions are unusual! ⚠️")

# Extra advice according the weather
if temp < 10 and is_raining:
    print("It's freezing and raining! Wear warm clothes and take an umbrella. ❄️")
elif temp > 35 and is_sunny:
    print("It's very hot! Stay hydrated and wear sunscreen. 🥵")
elif is_sunny and is_raining:
    print("It's a SUN-SHOWER! You might see a rainbow. 🌦️")
