# Python Simple Interest Calculator
# Formula:
#    SI = P * R * T / 100
#    Total Amount = P + SI
#    P = Principal amount
#    R = Rate of interest per annum
#    T = Time in years

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the number of years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Error: Principal, rate, and time must be non-negative values.")
else:
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print(f"\nThe simple interest on ${principal} at {rate}% per annum for {time} years is: ${simple_interest:.2f}")
    print(f"The total payable amount is: ${total_amount:.2f}")
