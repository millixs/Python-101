# Program to create a Countdown Timer in Python

# Why did we typecast my_time, minutes, and hours as int?
# We used int() because the / operator returns a float, and we need whole numbers for countdown calculations.
# If my_time is not converted to int, Python will throw a TypeError when comparing a string with a number.
# We may also receive incorrect output (e.g., 01:02.0833:40.5 instead of 01:02:40).

# Why didn’t we use int() for seconds?
# We didn’t use int() for seconds because the % operator always returns an integer when used with integers.
# x % 60 gives the remainder when x is divided by 60.
# Since x is always an integer (from the range() function), the result of x % 60 is already an integer, so int() is unnecessary.

import time  # Import the time module for sleep functionality

my_time = int(input("Enter the time in seconds: ").strip())

while my_time <= 0:  # prompts the user to enter a valid positive time
    print("Invalid time entered! Please enter a positive number.")
    my_time = int(input("Enter the time in seconds: ").strip())

for x in range(my_time, 0, -1):  # Iterates in reverse order; alternatively, reversed() can be used for the same effect
    seconds = x % 60  # Keeps seconds within the 0-59 range
    minutes = int(x / 60) % 60  # Keeps minutes within the 0-59 range since each minute has 60 seconds
    hours = int(x / 3600)  # Converts total seconds into hours; % 24 isn't needed as the program doesn't account for days

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # Displays the output in the format (hh:mm:ss) like a digital clock
    # Zero-padded (:02) for better readability

    time.sleep(1)  # Pause for 1 second to create countdown effect

print("\nTIME'S UP!!")  # After (my_time) seconds, the final message appears on the terminal
