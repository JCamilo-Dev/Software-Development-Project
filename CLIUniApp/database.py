
import os
import pickle

from models.student import Student


_DEFAULT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.data")


class Database:
    def __init__(self, path=None):
        self.path = path or _DEFAULT_PATH
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.path):
            with open(self.path, "wb") as f:
                pickle.dump([], f)
    def load_all(self):
        try:
            with open(self.path, "rb") as f:
                return pickle.load(f)
        except (EOFError, FileNotFoundError):
            return []

    def find_by_email(self, email):
        students = self.load_all()

        for student in students:
            if student.email == email:
               return student

        return None

    def add(self, student):
        students = self.load_all()
        students.append(student)

        with open(self.path, "wb") as f:
            pickle.dump(students, f)

    def remove(self, student_id):
        students = self.load_all()

        for student in students:
            if str(student.id) == str(student_id):
               students.remove(student)

            with open(self.path, "wb") as f:
                pickle.dump(students, f)

            return True

        return False
    def clear(self):
        with open(self.path, "wb") as f:
            pickle.dump([], f)
                
