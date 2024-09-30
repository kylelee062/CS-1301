import random  

rand_num = random.randint(1,100)
attempts = 10
print("I have generated a random number from 1 to 100. You have 10 attempts to guess.")

for attempt in range(attempts):
    guess = int(input("Guess: "))
    if guess == rand_num:
        print("You correctly guessed my random number!")
        break
    elif guess > rand_num:
        print("Your guess is greater than my number. Try again!")
    else:
        print("Your guess is less than my number. Try again!")
else:
    print("Sorry, you ran out of attempts :(")
        
