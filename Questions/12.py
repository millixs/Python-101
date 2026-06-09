# Python Compound Interest Calculator
# The formula for Compound Interest (CI) is:
#     CI = A − P
#     A = FinalAmount (Total payable amount after interest)
#     P = Principal amount
# Final Amount (A) is calculated using:
#     A = P * (1 + (R / 100)) ^ T
#     R = Rate of interest per annum
#     T = Time in years

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the number of years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Principal, rate, and time must be non-negative")
else:
    amount = principal * pow((1 + (rate / 100)), time)
    interest = amount - principal
    print(f"Final Amount: ${amount:.2f}")
    print(f"Compound Interest: ${interest:.2f}")
