"""Student model.

A student owns a list of Subject objects and a handful of scalar
fields (id, name, email, password). The model itself does not talk to
the database - persistence is the Database class's job. All we do here
is convert to and from plain dicts so pickle can store them.
"""



class Student:
    def __init__(self, sid, name, email, password, subjects=None):
        self.id = sid
        self.name = name
        self.email = email
        self.password = password
        self.subjects = list(subjects) if subjects else []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": [s.to_dict() for s in self.subjects],
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def average_mark(self):
        if not self.subjects:
            return 0.0
        return sum(s.mark for s in self.subjects) / len(self.subjects)

    def overall_grade(self):
        return 0

    def is_pass(self):
        return self.average_mark() >= 50

    def __repr__(self):
        return f"Student({self.id}, {self.name}, subjects={len(self.subjects)})"
