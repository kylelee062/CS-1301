# defines what each ingredient is
# print(f'{your_value:.2f}') for output of 2 digits
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
serving_size = float(input('How many servings does this make?\n'))


#prints the amount of servings and the cups for each ingredient
print('\nLemonade ingredients - yields {:.2f} servings'.format(serving_size))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar))

#part 2
servings = float(input("\nHow many servings would you like to make?\n"))

desired_servings = servings/serving_size
lemon_juice_cups *= desired_servings
water *= desired_servings
agave_nectar *= desired_servings

print("\nLemonade ingredients - yields {:.2f} servings".format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar))

#part 3
gallon = 16 #cups
lemon_juice_cups /= 16
water /= 16
agave_nectar /= 16

print("\nLemonade ingredients - yields {:.2f} servings".format(servings))
print('{:.2f} gallon(s) lemon juice'.format(lemon_juice_cups))
print('{:.2f} gallon(s) water'.format(water))
print('{:.2f} gallon(s) agave nectar'.format(agave_nectar))