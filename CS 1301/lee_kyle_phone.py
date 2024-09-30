number = int(input("Please enter your phone number: "))
area_code = number // 10000000
prefix = (number // 10000) % 1000
line = number % 10000

print(f"({area_code}) {prefix}-{line}")