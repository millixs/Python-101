# Program to print a shipping label (as seen on delivery packages) using both *args and **kwargs

# *args = allows us to pass a variable number of non-keyword arguments (e.g., title, first name, last name)
# **kwargs = allows us to pass a variable number of keyword arguments (e.g., address details like city, state, etc.)

def shipping_label(*args, **kwargs):
    # Print personal details (e.g., title, name parts) from *args
    for arg in args:
        print(arg, end=" ")
    print()

    # Check if both 'apt_no' and 'po_box_no' are present in the address
    if "apt_no" and "po_box_no" in kwargs:
        # .get() is a safe way to access values from kwargs; it returns the value for the specified key without raising a KeyError if the key doesn't exist
        print(f"{kwargs.get('house_name')} {kwargs.get('apt_no')}")
        print(f"{kwargs.get('landmark')}")
        print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
        print(f"PO Box No: {kwargs.get('po_box_no')}")
        print()
    else:
        # If apt_no or po_box_no is not provided, print a simplified address
        print(f"{kwargs.get('house_name')}")
        print(f"{kwargs.get('landmark')}")
        print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
        print()

# Example 1: Apartment number and PO box number are omitted
shipping_label("Ms.", "Milli", "Sood",
               house_name="Sansar Villa",
               # apt_no="02",
               # po_box_no="#2359",
               landmark="Near High Court",
               city="Shimla",
               state="H.P.",
               zip="171001")

# Example 2: Apartment number and PO box number are included
shipping_label("Ms.", "Milli", "Sood",
               house_name="Sansar Villa",
               apt_no="02",
               po_box_no="#2359",
               landmark="Near High Court",
               city="Shimla",
               state="H.P.",
               zip="171001")
