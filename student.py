
class Student:
    def __init__(self, name, student_id, grade=None):
        self.name = name
        self.student_id = student_id
        self.__grades = []

        if grade is not None:
            self.add_grades(grade)

    def get_grades(self):
        return self.__grades.copy()

    def add_grades(self, grade):
        if isinstance(grade, (int, float)) and not isinstance(grade, bool) and 0 <= grade <= 100:
            self.__grades.append(grade)
            return True
        else:
            print("Invalid grade. Grade must be between 0 and 100.")
            return False

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def calculate_grade(self):
        return self.calculate_average()

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self.__grades)
        print("Average Grade:", round(self.calculate_average(), 2))


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, major):
        super().__init__(name, student_id)
        self.major = major

    def display_info(self):
        print("\n--- Undergraduate Student ---")
        print("Major:", self.major)
        super().display_info()


class GraduateStudent(Student):
    def __init__(self, name, student_id, program_title):
        super().__init__(name, student_id)
        self.program_title = program_title

    def display_info(self):
        print("\n--- Graduate Student ---")
        print("Program Title:", self.program_title)
        super().display_info()


student1 = Student("Mohamed Ahmed", "MH2500510", 100)
student1.add_grades(85)
student1.add_grades(90)

student1.display_info()


undergraduate = UndergraduateStudent(
    "Ahmed Ali", "UG001", "Electronic Engineering"
)

graduate = GraduateStudent(
    "Sara Mohamed", "PG001", "Computer Engineering"
)

# Add three grades to the undergraduate student
undergraduate.add_grades(85)
undergraduate.add_grades(90)
undergraduate.add_grades(95)

# Add three grades to the graduate student
graduate.add_grades(80)
graduate.add_grades(88)
graduate.add_grades(92)

# Display student information
undergraduate.display_info()
graduate.display_info()


def Grades_sort(students):
    return sorted(students, key=lambda student: student.calculate_average())

# Sort students according to their average grades
students = [student1, undergraduate, graduate]

sorted_students = Grades_sort(students)

print("\n--- Students Sorted by Average Grade (Ascending) ---")

for student in sorted_students:
    student.display_info()
