class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grade:", self.grade)


student1 = Student("Mohamed Ahmed", "MH2500510", 100)

student1.display_info()
