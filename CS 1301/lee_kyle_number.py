class Number:
    def __init__(self,num):
        self.num = num
    
    def __str__(self):
        return str(self.num)
    
    def __add__(self, other):
        return (self.num + other.num)
    
    def __sub__(self, other):
        return (self.num - other.num)
    
    def __mul__(self, other):
        return (self.num * other.num)
    
    def __truediv__(self, other):
        return (self.num // other.num)
    

num1 = int(input())
num2 = int(input())

a = Number(num1)
b = Number(num2)

add_sum = a + b
print(f"{a} + {b} = {add_sum}")

sub_sum = a - b
print(f"{a} - {b} = {sub_sum}")

mult_prod = a * b
print(f"{a} * {b} = {mult_prod}")

div_prod = a / b
print(f"{a} / {b} = {div_prod}")

total = (add_sum + (sub_sum * mult_prod)) / div_prod
print(f"({add_sum} + ({sub_sum} * {mult_prod})) / {div_prod}")
