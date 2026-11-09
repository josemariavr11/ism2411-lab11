# Reflection 1:
# I would use .get() when I am not sure if a key exists,
# because it prevents errors and lets me use a default value.
# I would use bracket notation when I know the key should exist.

# Reflection 2:
# Exercise 8 reminds me of using a PivotTable in Excel to
# summarize sales by category or region. Python can be more
# useful for large datasets because it can automate the process
# and handle information without manually organizing it.


# Exercise 1

customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2

customer["phone"] = "813-555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

# Using .items() gives us both keys and values.
# Without .items(), the loop only gives us the keys.

# Exercise 5

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

original_price = 200
final_price = original_price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final Price: ${final_price:.2f}")

# Exercise 6

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)

    discount_amount = 300 * discount

    print(f"{name} ({tier}): ${discount_amount:.2f} discount")

# Exercise 7

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} has {details['stock']} units left")

# Exercise 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")

