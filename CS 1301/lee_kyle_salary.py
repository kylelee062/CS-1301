wage = int(input("Please enter your hourly wage: "))
hours = int(input("Please enter the number of hours worked per week: "))
weeks = int(input("Please enter the number of weeks worked this year: "))
salary = (wage * hours) * weeks

print("Your salary so far this year is ${}".format(salary))