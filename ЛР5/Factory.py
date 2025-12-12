from abc import ABC, abstractmethod
import unittest

class UniversityMember(ABC):
    @abstractmethod
    def get_role(self):
        pass

class Professor(UniversityMember):
    def get_role(self):
        return "Professor"

class Student(UniversityMember):
    def get_role(self):
        return "Student"

class MemberFactory(ABC):
    @abstractmethod
    def create_member(self):
        pass

class ProfessorFactory(MemberFactory):
    def create_member(self):
        return Professor()

class StudentFactory(MemberFactory):
    def create_member(self):
        return Student()

def client_code(factory: MemberFactory):
    member = factory.create_member()
    print(f"Created a university member with role: {member.get_role()}")

class TestMemberFactory(unittest.TestCase):
    def test_professor_factory(self):
        factory = ProfessorFactory()
        prof = factory.create_member()
        self.assertEqual(prof.get_role(), "Professor")

    def test_student_factory(self):
        factory = StudentFactory()
        student = factory.create_member()
        self.assertEqual(student.get_role(), "Student")

if __name__ == "__main__":
    client_code(ProfessorFactory())
    client_code(StudentFactory())
    print("\nRunning tests...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
