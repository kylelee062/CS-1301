menu_item = {
    "Hot Dogs": 1.50,
    "Slice of Pizza" : 1.99,
    "Whole Pizza" : 9.95,
    "Soft Drink" : 0.59

}
hot_dog = int(input("Please enter the number of Hot dogs: "))
slices = int(input("\nPlease enter the number of Pizza Slices: "))
whole_pizza = int(input("\nPlease enter the number of Whole Pizzas: "))
drinks = int(input("\nPlease enter the number of Soft Drinks: "))

total_cost = (
    (menu_item["Hot Dogs"]*hot_dog) + (menu_item["Slice of Pizza"]*slices) + (menu_item["Whole Pizza"]*whole_pizza) + (menu_item["Soft Drink"]*drinks)
)

print(f'\nThe total cost of the order is ${total_cost:.2f}')