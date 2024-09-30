def is_power_of_two(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n <= 0:
        return False
    else:
        return is_power_of_two(n // 2)

try:
    input_number = int(input("Enter an integer: "))
    
    result = is_power_of_two(input_number)
    print(f"Output: {str(result).lower()}")
    print(f"Explanation: 2^0 = {input_number}" if result else f"Explanation: {input_number} is not a power of two.")
except ValueError:
    print("Invalid input. Please enter an integer.")
