import math
side_a =  float(input("Please enter the length of Side A of the triangle (in meters): "))
side_b =  float(input("Please enter the length of Side B of the triangle (in meters): "))
side_c =  float(input("Please enter the length of Side C of the triangle (in meters): "))

perimeter = side_a + side_b + side_c
semi_perimeter =  (side_a + side_b + side_c) / 2
area = math.sqrt(semi_perimeter*(semi_perimeter-side_a)*(semi_perimeter-side_b)*(semi_perimeter-side_c))
pythagorean_theorem = (side_a ** 2) + (side_b ** 2) 


print(f'The perimeter of the triangle is: {perimeter}m')
print(f'The area of the triangle is: {area:.2f}m^2')

if pythagorean_theorem == (side_c ** 2):
    print('It is a Right Triangle.')
elif pythagorean_theorem > (side_c ** 2): 
    print('It is an Acute Triangle.')
else:
    print('It is an Obtuse Triangle.')
