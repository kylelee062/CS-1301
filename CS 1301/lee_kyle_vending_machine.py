class VendingMachine:
    def __init__(self, num_water, num_soda, num_coffee):
        self.water = num_water
        self.soda = num_soda
        self.coffee = num_coffee
    
    def buy(self, drink_type):
        if drink_type == "1" and self.water > 0:
            self.water -= 1
        elif drink_type == "2" and self.soda > 0:
            self.soda -= 1
        elif drink_type == "3" and self.coffee > 0:
            self.coffee -= 1
        else:
            print("Requested drink not available.")

    def restock(self, drink_type, stock):
        if drink_type == "1":
            self.water += stock
        elif drink_type == "2":
            self.soda += stock
        elif drink_type == "3":
            self.coffee += stock

    def inventory(self):
        print("\nInventory")
        print(f"Water: {self.water} bottles")
        print(f"Soda: {self.soda} bottles")
        print(f"Coffee: {self.coffee} bottles")


vending = VendingMachine(10, 10, 10)
stop_words = ['quit','q']
while True:
    drink = input("\nPlease select an option: buy, restock, or inventory: ")
    if drink == "buy":
        drink_type = input("\nPlease select an option: \n1 - Water\n2 - Soda \n3 - Coffee\n")
        vending.buy(drink_type)
    elif drink == "inventory":
        vending.inventory()
    elif drink == "restock":
        drink_type = input("\nPlease select an option: \n1 - Water\n2 - Soda \n3 - Coffee\n")
        stock = int(input("Enter the number of bottles to restock: "))
        vending.restock(drink_type, stock)
    elif drink in stop_words:
        break
    else:
        print("Invalid input. Please try again.")
