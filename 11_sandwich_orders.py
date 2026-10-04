sandwich_orders = ['burger', 'pastry', 'butter']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print(f"\nFinished sandwiches: {finished_sandwiches}")
