item = (input("Enter food item name:\n"))
price = float(input("Enter item price:\n"))
quantity = int(input("Enter item quantity:\n"))
total = quantity * price
total_cost = total

print("\nRECEIPT")
print(f"{quantity} {item} @ ${price:.2f} = ${total:.2f}")
print(f"Total cost: ${total_cost:.2f}\n")

item2 = (input("Enter food item name:\n"))
price2 = float(input("Enter item price:\n"))
quantity2 = int(input("Enter item quantity:\n"))
total2 = quantity2 * price2
total_cost += total2

print("\nRECEIPT")
print(f"{quantity} {item} @ ${price:.2f} = ${total:.2f}")
print(f"{quantity2} {item2} @ ${price2:.2f} = ${total2:.2f}")
print(f"Total cost: ${total_cost:.2f}")

graduity = total_cost * 0.15
total_with_tip = graduity + total_cost
print(f"\n15% Graduity: ${graduity:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
