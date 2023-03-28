from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Dimitar", {"Python-OOP": ["Exam prep", "Exam prep", "Reg exam"]})

    def test_successful_initialization(self):
        self.assertEqual("Dimitar", self.student.name)
        self.assertEqual({"Python-OOP": ["Exam prep", "Exam prep", "Reg exam"]}, self.student.courses)

    def test_enroll_course_exists(self):
        result = self.student.enroll("Python-OOP", ["Retake exam"])
        self.assertEqual(["Exam prep", "Exam prep", "Reg exam", "Retake exam"], self.student.courses["Python-OOP"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_add_course_notes(self):
        result = self.student.enroll("PY WEB", ["Django", "Flask"])
        self.assertEqual(["Django", "Flask"], self.student.courses["PY WEB"])
        self.assertEqual("Course and course notes have been added.", result)


    def test_enroll_without_notes(self):
        result = self.student.enroll("Basics", ["Some Note"], "No")
        self.assertEqual([], self.student.courses["Basics"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python-Fund", ["Some", "Notes"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_successful_add_notes(self):
        result = self.student.add_notes("Python-OOP", "Workshop")
        self.assertEqual(["Exam prep", "Exam prep", "Reg exam", "Workshop"], self.student.courses["Python-OOP"])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_exception_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python-Fund")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_successful_leave_course(self):
        result = self.student.leave_course("Python-OOP")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == '__main__':
    main()
