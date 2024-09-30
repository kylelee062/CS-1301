grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
day1 = {"Mary", "Jake", "Sam", "Alex", "Percy", "Jessica", "Trent", "Mahamoud"}
day2 = {"Jake","Sam","Alex","Percy","Mahamoud","Trent","Caleb","Zayne"}

num_students = len(grades)
max_grade = max(grades)
min_grade = min(grades)
avg_grade = sum(grades) / 12
print(f'{num_students} Students took the exam.')
print(f'The highest grade was a {max_grade}.')
print(f'The lowest grade was a {min_grade}.')
print(f'The average grade for the exam was a {avg_grade:.1f}.\n')

students_attended = len(day1.union(day2))
both_days = day1.intersection(day2)
one_day = day1.symmetric_difference(day2)

print(f'{students_attended} students attended the class.')
print(f'{both_days} attended both class days.')
print(f'{one_day} attended one class day.')




