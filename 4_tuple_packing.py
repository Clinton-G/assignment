def print_order_details(orders):
    for order in orders:
        customer_name, product, quantity = order
        print('Customer:', customer_name, '\nProduct:', product, '\nQuantity:', quantity, '\n-  -  -  -  -')

# Sample Order Data
orders = [
    ("John", "Laptop", 1),
    ("Bob", "Camera", 10),
    ("Charlie", "Headphones", 2),
    ("David", "Monitor", 3)
]

# Print order details
print_order_details(orders)
