hexa_value = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def Hex_to_RGB(hexa_thing, hexa_value):
    hexa_thing = hexa_thing.strip('#')

    r = hexa_value[hexa_thing[0].upper()] * 16 + hexa_value[hexa_thing[1].upper()]
    g = hexa_value[hexa_thing[2].upper()] * 16 + hexa_value[hexa_thing[3].upper()]
    b = hexa_value[hexa_thing[4].upper()] * 16 + hexa_value[hexa_thing[5].upper()]

    return {'R': r, 'G': g, 'B': b}


stop_words = ['quit', 'q']
while True:
    print("Hex to RGB")
    print("Type quit or q to exit the program!")
    hex_code = input("Enter a hexadecimal RGB Code: ")
    if hex_code in stop_words:
        break
    rgb_dict = Hex_to_RGB(hex_code, hexa_value)
    print("\nRGB Values")
    print(f"Red: {rgb_dict['R']}")
    print(f"Green: {rgb_dict['G']}")
    print(f"Blue: {rgb_dict['B']}\n")