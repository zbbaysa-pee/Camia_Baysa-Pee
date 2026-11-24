food_orders = []
for i in range(1, 6):
    order = input(f"Enter Order {i}: ")
    food_orders.append(order)
print(f"Original Orders: {food_orders}")
additional_order = input("Enter additiontal order: ")
food_orders.append(additional_order)
print(f"Updated Orders: {food_orders}")
priority_order = input("Enter priority order: ")
food_orders.insert(0, priority_order)
print(f"Updated Orders: {food_orders}")

search = input("Search for an order: ")
occurence = food_orders.count(search)
if occurence > 0:
    print(f"Number of occurences: {occurence}")
    print(f"First Index: {food_orders.index(search)}")
else:
    print("Order not found")

cancel_order = input("Enter order to cancel: ")
food_orders.remove(cancel_order)
print(f"Updated Orders: {food_orders}")

last_order = food_orders.pop()
print(f"Last Order Removed: {last_order}")

print("===== FINAL ORDER REPORT =====")
print(food_orders)
print(f"Total Remaining Orders: {len(food_orders)}")
