
import json
import os


# ==========================================
# 1. STUDENT CLASSES
# ==========================================

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []

    def get_grades(self):
        return self.__grades.copy()

    def add_grades(self, grade):
        if isinstance(grade, (int, float)) and not isinstance(grade, bool) and 0 <= grade <= 100:
            self.__grades.append(grade)
            return True

        print("Invalid grade. Enter a value between 0 and 100.")
        return False

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0

        return sum(self.__grades) / len(self.__grades)

    def calculate_grade(self):
        return self.calculate_average()

    def display_info(self):
        print("\nStudent Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self.get_grades())
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


# ==========================================
# 2. FILE HANDLING
# ==========================================

DATA_FILE = "students.txt"


def save_students(students, filename=DATA_FILE):
    student_data = []

    for student in students:
        data = {
            "type": type(student).__name__,
            "name": student.name,
            "student_id": student.student_id,
            "grades": student.get_grades()
        }

        if isinstance(student, UndergraduateStudent):
            data["major"] = student.major

        elif isinstance(student, GraduateStudent):
            data["program_title"] = student.program_title

        student_data.append(data)

    try:
        with open(filename, "w") as file:
            json.dump(student_data, file, indent=4)

        print("\nStudent records saved successfully.")

    except OSError as error:
        print("Could not save student records:", error)


def read_students(filename=DATA_FILE):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            student_data = json.load(file)

        if not isinstance(student_data, list):
            print("Invalid database format.")
            return []

        students = []

        for data in student_data:
            student_type = data.get("type")

            if student_type == "UndergraduateStudent":
                student = UndergraduateStudent(
                    data["name"],
                    data["student_id"],
                    data["major"]
                )

            elif student_type == "GraduateStudent":
                student = GraduateStudent(
                    data["name"],
                    data["student_id"],
                    data["program_title"]
                )

            elif student_type == "Student":
                student = Student(
                    data["name"],
                    data["student_id"]
                )

            else:
                print("Unknown student type. Record skipped.")
                continue

            for grade in data.get("grades", []):
                student.add_grades(grade)

            students.append(student)

        return students

    except FileNotFoundError:
        return []

    except (json.JSONDecodeError, KeyError, TypeError, OSError) as error:
        print("Could not read student records:", error)
        return []


# ==========================================
# 3. STUDENT MANAGEMENT FUNCTIONS
# ==========================================

def find_student(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student

    return None


def add_student(students):
    print("\n--- Register New Student ---")

    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    if not name or not student_id:
        print("Name and student ID cannot be empty.")
        return

    if find_student(students, student_id) is not None:
        print("A student with this ID already exists.")
        return

    print("\nSelect student type:")
    print("1. Regular Student")
    print("2. Undergraduate Student")
    print("3. Graduate Student")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        student = Student(name, student_id)

    elif choice == "2":
        major = input("Enter major: ").strip()

        if not major:
            print("Major cannot be empty.")
            return

        student = UndergraduateStudent(name, student_id, major)

    elif choice == "3":
        program_title = input("Enter program title: ").strip()

        if not program_title:
            print("Program title cannot be empty.")
            return

        student = GraduateStudent(name, student_id, program_title)

    else:
        print("Invalid student type.")
        return

    students.append(student)
    print("Student registered successfully.")


def add_student_grades(students):
    student_id = input("Enter student ID: ").strip()

    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    try:
        grade = float(input("Enter grade (0-100): "))

        if student.add_grades(grade):
            print("Grade added successfully.")

    except ValueError:
        print("Please enter a valid number.")


def display_students(students):
    if not students:
        print("\nNo student records available.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:
        student.display_info()


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
    else:
        print("\nStudent found:")
        student.display_info()


def calculate_student_average(students):
    student_id = input("Enter student ID: ").strip()

    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
    else:
        print(
            "Average Grade:",
            round(student.calculate_average(), 2)
        )


def Grades_sort(students):
    return sorted(
        students,
        key=lambda student: student.calculate_average()
    )


def sort_students(students):
    if not students:
        print("No students available to sort.")
        return

    sorted_students = Grades_sort(students)

    print("\n--- Students Sorted by Average Grade (Ascending) ---")

    for student in sorted_students:
        student.display_info()


# ==========================================
# 4. TEACHER MENU
# ==========================================

def display_menu():
    print("\n" + "=" * 45)
    print("       STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add a student")
    print("2. Add grades")
    print("3. Display all students")
    print("4. Search for a student")
    print("5. Calculate student average")
    print("6. Sort students by average")
    print("7. Save student records")
    print("8. Exit")
    print("=" * 45)


# ==========================================
# 5. MAIN PROGRAM
# ==========================================

def main():
    students = read_students()

    print("\nWelcome to the Student Grade Management System!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            add_student_grades(students)

        elif choice == "3":
            display_students(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            calculate_student_average(students)

        elif choice == "6":
            sort_students(students)

        elif choice == "7":
            save_students(students)

        elif choice == "8":
            save_students(students)
            print("\nThank you for using the application!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
