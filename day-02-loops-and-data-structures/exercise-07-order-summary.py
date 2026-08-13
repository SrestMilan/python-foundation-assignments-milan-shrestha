
"""
Exercise: Nested Order Summary
Student: Milan Shrestha
Day: 2
"""

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID alongside its customer name
for order_ref, order_info in orders.items():
    print(f"{order_ref}: {order_info['customer']}")

# 2. Print only the orders whose status is "Completed"
print("\nCompleted orders:")
for order_ref, order_info in orders.items():
    if order_info["status"] == "Completed":
        print(f"{order_ref}: {order_info}")

# 3. Sum the amount for every completed order (generator expression inside sum())
completed_revenue = sum(
    order_info["amount"]
    for order_info in orders.values()
    if order_info["status"] == "Completed"
)

# 4. Count how many orders are still pending
pending_count = sum(
    1
    for order_info in orders.values()
    if order_info["status"] == "Pending"
)

# 5. Add a new order to the existing dictionary (nested dict, same structure as the rest)
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 1500,
    "status": "Pending"
}

print(f"\nTotal amount from completed orders: {completed_revenue}")
print(f"Number of pending orders: {pending_count}")
print(f"\nUpdated orders dictionary: {orders}")