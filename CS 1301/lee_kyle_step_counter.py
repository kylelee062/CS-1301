def steps_to_miles(num_steps):
    try:
        num_steps = float(num_steps)
    except ValueError:
        raise ValueError("Exception: Non-Numeric step count entered.")

    if num_steps < 0:
        raise ValueError("Exception: Negative step count entered.")

    return num_steps / 2000

num_steps = input("Enter # of steps: ")
try:
    num_miles = steps_to_miles(num_steps)
    print('{:.2f} miles'.format(num_miles))
except ValueError as i:
    print(i)

