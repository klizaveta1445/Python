from abc import ABC, abstractmethod
import unittest

class Person(ABC):
    def __init__(self, role_impl):
        self._role_impl = role_impl

    @abstractmethod
    def perform_duty(self):
        pass

class RoleImpl(ABC):
    @abstractmethod
    def duty(self):
        pass

class StudentRole(RoleImpl):
    def duty(self):
        return "Студент учится и выполняет домашние задания."

class TeacherRole(RoleImpl):
    def duty(self):
        return "Преподаватель читает лекции и проверяет работы."

class Student(Person):
    def perform_duty(self):
        return self._role_impl.duty()

class Teacher(Person):
    def perform_duty(self):
        return self._role_impl.duty()

class TestUniversityBridge(unittest.TestCase):

    def test_student_duty(self):
        student_role = StudentRole()
        student = Student(student_role)
        self.assertEqual(student.perform_duty(), "Студент учится и выполняет домашние задания.")

    def test_teacher_duty(self):
        teacher_role = TeacherRole()
        teacher = Teacher(teacher_role)
        self.assertEqual(teacher.perform_duty(), "Преподаватель читает лекции и проверяет работы.")

    def test_role_swap(self):
        student_role = StudentRole()
        teacher_role = TeacherRole()
        person = Student(student_role)
        self.assertEqual(person.perform_duty(), "Студент учится и выполняет домашние задания.")
        person._role_impl = teacher_role
        self.assertEqual(person.perform_duty(), "Преподаватель читает лекции и проверяет работы.")

if __name__ == "__main__":
    student = Student(StudentRole())
    teacher = Teacher(TeacherRole())

    print("Студент:", student.perform_duty())
    print("Преподаватель:", teacher.perform_duty())
    print()

    print("Запуск тестов...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
