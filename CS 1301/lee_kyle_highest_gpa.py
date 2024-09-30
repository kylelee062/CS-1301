# Creating custom error class
class EmptyRosterError(Exception):
    pass

class Student:
    def __init__(self, first_name, last_name, GPA):
        self.first = first_name
        self.last = last_name
        self.gpa = GPA

    def get_gpa(self):
        return self.gpa
    
    def get_first(self):
        return self.first
    
    def get_last(self):
        return self.last

class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)
    
    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty")
        highest_gpa_student = max(self.roster, key=lambda x: x.get_gpa())
        return highest_gpa_student

def main():
    course = Course()
    stop_words = ["quit", "q"]
    while True:
        try:
            print("\nWelcome to CSC 1301!")
            print("Please add students to the Course! (quit or q to exit)\n")
            input_first = input("Enter First Name: ")
            if input_first.lower() in stop_words:
                break
            input_last = input("Enter Last Name: ")
            if input_last.lower() in stop_words:
                break
            input_GPA = float(input("Enter GPA: "))

            student = Student(input_first, input_last, input_GPA)
            course.add_student(student)

        except ValueError:
            print("Error: Enter a Numeric value")
    
    print(f"\nCourse Size: {course.course_size()}")  
    try:
        highest_gpa_student = course.find_student_highest_gpa()
        print(f"Highest GPA: {highest_gpa_student.get_gpa()}")
        print(f"Student with highest GPA: {highest_gpa_student.get_first()} {highest_gpa_student.get_last()}")
    except EmptyRosterError as e:
        print(e)

if __name__ == "__main__":
    main()
