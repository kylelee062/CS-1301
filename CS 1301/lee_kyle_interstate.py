def highway(interstate_numbers):
    direction = "none"
    if 1 <= interstate_numbers <= 99:
        if interstate_numbers % 2 == 1:
            print(f"I-{interstate_numbers} is primary, going north/south.")
        else:
            print(f'I-{interstate_numbers} is primary, going east/west.')
    elif 100 <= interstate_numbers <= 999:
        primary = interstate_numbers % 100
        if 1 <= primary <= 99:
            if primary % 2 == 1:
                direction = "north/south"
            else: 
                direction = "east/west"
            return(f'I-{interstate_numbers} is auxiliary, serving I-{primary}, going {direction}')
        else: 
            return(f"{interstate} is not a valid interstate highway number.")
        
interstate = int(input("Please enter an interstate number: "))
result = highway(interstate)
print(result)
