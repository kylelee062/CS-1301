def median(first, second, third):
    if second < first < third or third < first < second:
        return(first)
    elif first < second < third or third < second < first:
        return(second)
    elif first < third < second or second < third < first:
        return(third)
    else:
        return(None)
first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
third = int(input("Please enter the third number: "))

result = median(first,second,third)
print(f"the median is {result}")
