number = int(input('Please enter the number of floating-point values: '))

values = []
for i in range(number):
    value = float(input('Please enter a floating-point value: '))
    values.append(value)

max_value = max(values)

print('Normalized Floating-Point Values:')
for value in values:
    new_value = value / max_value
    print(f'{new_value:.2f}')
