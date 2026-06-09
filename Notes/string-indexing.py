# Indexing: Accessing elements of a sequence using [] (indexing operator)
#           Format: [start : end : step]

# start: The index from where the slicing begins (default is 0).
# end: The index where slicing stops (default is the end of the string).
# step: Determines how many characters to skip while moving through the string

credit_number = "5129-6708-0085-1980"  # Indexing starts from 0

print(credit_number[7])  # Prints the character at index 7
# (If only one number is inside [], it refers to a single index position)

print(credit_number[0:9])  # Prints characters from index 0 to 8 (9th index is exclusive)

print(credit_number[5:13])  # Prints characters from index 5 to 12

print(credit_number[:3])  # Omitting start index → Defaults to 0 (prints first 3 characters)

print(credit_number[0:])  # Omitting end index → Defaults to the end of the string (prints full string)

print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}")  # Negative indexing → Counts from the end (-1 is last char, -2 is second last, etc.)
# This is useful for masking a card number, displaying only the last 4 digits for privacy.

print(credit_number[::-1])  # Reverses the string, printing the credit number backward

print(credit_number[::3])  # Step index of 3 → Skips every second character
# EXPLANATION:-
# start is omitted → Defaults to 0 (start from the beginning).
# end is omitted → Defaults to the last character (go till the end).
# step = 3 → This means:
# Start at index 0
# Pick the character at index 0
# Skip 2 characters, then pick the next character (index 3)
# Skip 2 characters, then pick the next character (index 6)
# Continue this pattern till the end of the string
