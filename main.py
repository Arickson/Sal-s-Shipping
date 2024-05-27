# Prompts
service = input("What type of service is needed? (Ground/Premium/Drone): ")
weight = float(input("Enter the weight of the package in pounds: "))

# Defining variables
price = 0

# Ground Shipping
if service == "Ground":
    price = 20
    if weight <= 2:
        price += 1.5 * weight
    elif weight <= 6:
        price += 3 * weight
    elif weight <= 10:
        price += 4 * weight
    else:
        price += 4.75 * weight

# Premium Shipping
elif service == "Premium":
    premium_ground = 125
    print(premium_ground)

# Drone Shipping
elif service == "Drone":
    if weight <= 2:
        price += 4.5 * weight
    elif weight <= 6:
        price += 9 * weight
    elif weight <= 10:
        price += 12 * weight
    else:
        price += 12.25 * weight

print("Total Price: $", price)