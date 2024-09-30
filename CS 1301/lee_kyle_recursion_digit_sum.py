def recursive_digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + recursive_digit_sum(n // 10)

input_number = int(input())
result = recursive_digit_sum(input_number)
print(f"Result: {result}")
print(f"Explanation: {'+'.join(str(digit) for digit in map(int, str(input_number)))} = {result}")

