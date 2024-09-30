# 1.More practice with return including returning None
# 2.Contitionals
    # a. if 
    # b. else
    # c. elif
# 3.Relational operators == < > <= >= !=
# 4.and, or, not
# 5. Fuctions that return a boolean value

print(None)
print(type(None))

def circ_area(radius):
    area = 3.141519 * radius ** 2
    return area

result = circ_area(5)
print(round(result,2))

##### boolan expressions evalute to True or False

print(3>5)

# the equality comparison is done using ==

num = 3
print(num == 3)
print("cat" == "Cat")
print(3 == 3.4)
print("cat" < "dog")
print("aaa" < "baa")
# order of characters is determined by the AScii code which you do 
# not needto know for 1301

# you can ccombine these using and or not

print(3 < 5 and 3 > 2) # and requires both values to evaluate to True
print(3 < 5 or 3 < 1) # or requires one or both values to evaluate to True

# precedence of these conditional expressions work like this
# anythig in parenthesis is done first
# any arithmetic
# first the conditional (< <= etc) get evaluated
# then not then and then or
# lastly the assignment operator

value = 3 > 5 and not (2 < 7 or 9 > 1)
print(value)

print((3 < 2+1))

# write a statement that prints True if the number num is between 4 and 7 inclusive
num = 5
print(num >= 4 and num <= 7)
#print(num >= 4 and <= 7)

age = 4
if age >= 18 and age <= 99:
    print("Go vote!")
    print("Vote for cs1301 as the best class!")
else:
    print("No voting for you :(")
print("done")

if True:
    print("always")

if age > 17:
    print("you can go to college")
elif age >= 14:
    print("You can go to high school")
else:
    print("No school for you :(")

print("done done")

### num -= 1 sub

# The short cut to writing boolean is ==
def hello(flag):
    if flag == True:
        print("Hi")
    else:
        print("Bye")
    return flag
hello(False)

# To write "not" you say not_var or !var

flag = False
if (not flag):
    print("YES!")

