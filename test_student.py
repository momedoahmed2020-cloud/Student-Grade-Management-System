
import unittest
from student import Student, UndergraduateStudent, save_students, read_students


class TestStudent(unittest.TestCase):

    # Test 1: Calculate average with valid grades
    def test_calculate_average(self):
        student = Student("Mohamed", "MH001")
        student.add_grades(80)
        student.add_grades(90)

        self.assertEqual(student.calculate_average(), 85)

    # Test 2: Reject invalid grades
    def test_invalid_grades(self):
        student = Student("Ahmed", "AH001")

        result = student.add_grades(120)

        self.assertFalse(result)
        self.assertEqual(student.get_grades(), [])

    # Test 3: Calculate average with no grades
    def test_no_grades(self):
        student = Student("Ali", "AL001")

        self.assertEqual(student.calculate_average(), 0)

    # Test 4: Save and read student records
    def test_read_students(self):
        student = UndergraduateStudent(
            "Omar", "OM001", "Electronic Engineering"
        )
        student.add_grades(78)
        student.add_grades(85)

        filename = "test_students.txt"

        save_students([student], filename)
        students = read_students(filename)

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Omar")
        self.assertEqual(students[0].get_grades(), [78, 85])
        self.assertEqual(students[0].major, "Electronic Engineering")

    # Test 5: Handle a missing file
    def test_missing_file(self):
        students = read_students("missing_test_file.txt")

        self.assertEqual(students, [])


if __name__ == "__main__":
    unittest.main()
