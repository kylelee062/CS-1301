def feet_to_steps(feet):
    steps = feet / 2.5
    return int(steps)

feets = float(input("Please enter the distance traveled in feet: "))
steps_convertred = feet_to_steps(feets)
print(steps_convertred,"steps")