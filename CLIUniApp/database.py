
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
                