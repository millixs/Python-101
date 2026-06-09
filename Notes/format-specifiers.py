# Format Specifiers in f-strings:
# They allow us to format values in a specific way using flags.
# SYNTAX:  {value:flags}

# NOTE → Use print(variable, end=" ") to display the output on the same line, separated by spaces, dashes, or other characters.
# NOTE → Use print() to create a new line (add space)
# NOTE → Use "\n" to create a new line within a string
# :.nf  → Round to 'n' decimal places (fixed-point representation)
# :n    → Allocate at least 'n' spaces for the value (right-aligned by default)
# :0n   → Allocate 'n' spaces and zero-pad the value if needed
# :<    → Left-align the value within the allocated space
# :>    → Right-align the value within the allocated space
# :^    → Center-align the value within the allocated space
# :+    → Always show the sign (+ for positive, - for negative)
# :     → Add a space before positive numbers for alignment
# :=    → Place the sign at the leftmost position before padding
# :,    → Use a comma as a thousand separator
# :+,.nf → Mix multiple flags (e.g., sign, comma separator, decimal places)

price1 = 1230.13325
price2 = -4400.324
price3 = 64300.22

# Round to 2 decimal places
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}\n")

# Allocate 10 spaces (right-aligned by default)
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}\n")

# Allocate 3 spaces and zero-pad
print(f"Price 1 is ${price1:03}")
print(f"Price 2 is ${price2:03}")
print(f"Price 3 is ${price3:03}\n")

# Left-align in a field of 10 spaces
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}\n")

# Right-align in a field of 10 spaces
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}\n")

# Center-align in a field of 10 spaces
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}\n")

# Always show the sign (+ for positive, - for negative)
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}\n")

# Add a space before positive numbers for better alignment with negatives
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }\n")

# Sign placed at the leftmost position, then padding
print(f"Price 1 is ${price1:=10}")
print(f"Price 2 is ${price2:=10}")
print(f"Price 3 is ${price3:=10}\n")

# Allocate 2 spaces
print(f"Price 1 is ${price1:2}")
print(f"Price 2 is ${price2:2}")
print(f"Price 3 is ${price3:2}\n")

# Add a comma separator for thousands
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}\n")

# Mix multiple specifiers: Show sign, use comma separator, and round to 2 decimal places
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}\n")
