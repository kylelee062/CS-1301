cents = int(input("Please enter a number of cents: "))

quarters = cents // 25
cents %= 25

dimes = cents // 10 
cents %= 10

nickels = cents // 5