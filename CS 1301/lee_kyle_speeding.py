"""
speed_limit = int(input('Please enter the speed limit for the road: '))
recorded_speed = int(input("Please enter the vehicle's speed: "))
ticket = 0
difference = recorded_speed - speed_limit 

if difference  < 0:
    ticket = 50
    print(f'The speeding fine is ${ticket}.')
elif 6 <= difference <= 20:
    ticket = 75
    print(f'The speeding fine is ${ticket}.')
elif 21 <= difference <= 40:
    ticket = 150
    print(f'The speeding fine is ${ticket}.')
elif difference > 40:
    ticket = 300
    print(f'The speeding fine is ${ticket}.')
else:
    print("There is no fine")
"""
def ticket_price(difference):
    ticket = 0
    if difference  < 0:
        ticket = 50
        return(f'The speeding fine is ${ticket}.')
    elif 6 <= difference <= 20:
        ticket = 75
        return(f'The speeding fine is ${ticket}.')
    elif 21 <= difference <= 40:
        ticket = 150
        return(f'The speeding fine is ${ticket}.')
    elif difference > 40:
        ticket = 300
        return(f'The speeding fine is ${ticket}.')
    else:
        return("There is no fine")
    
speed_limit = int(input('Please enter the speed limit for the road: '))
recorded_speed = int(input("Please enter the vehicle's speed: "))
difference = recorded_speed - speed_limit 
result = ticket_price(difference)
print(result)