"""Admin controller for the CLI University System."""

from utils.term import say, ask, GREEN, YELLOW, RED
from database import Database

INDENT = " " * 8
ADMIN_PROMPT = INDENT + "Admin System (l/x): "


def run():
    db = Database()

    while True:
        choice = ask(ADMIN_PROMPT, GREEN).strip().lower()

        if choice == "l":
            _login(db)
        elif choice == "x":
            return


def _login(db):
    say(INDENT + "Admin Sign In", GREEN)

    username = ask(INDENT + "Staff username: ")
    password = ask(INDENT + "Staff password: ")

    # Pre-defined admin credentials
    if username == "admin" and password == "Admin123":
        say(INDENT + "Admin login successful", YELLOW)
        _admin_menu(db)
    else:
        say(INDENT + "Incorrect admin credentials", RED)


def _admin_menu(db):
    while True:
        say(INDENT + "Admin Menu", GREEN)
        say(INDENT + "1. View all students")
        say(INDENT + "2. View students by grade")
        say(INDENT + "3. Categorize PASS/FAIL")
        say(INDENT + "4. Remove student")
        say(INDENT + "5. Clear student data")
        say(INDENT + "X. Exit")

        choice = ask(INDENT + "Select an option: ").strip().lower()

        if choice == "1":
           _view_all_students(db)
        elif choice == "2":
           _view_students_by_grade(db)  
        elif choice == "3":
            _categorize_students(db)
        elif choice == "4":
            _remove_student(db)
        elif choice == "5":
            _clear_student_data(db)
        elif choice == "x":
            return



def _view_all_students(db):
    say(INDENT + "All Students", GREEN)

    students = db.load_all()

    if not students:
        say(INDENT + "No students found", YELLOW)
        return

    for student in students:
        say(
            INDENT
            + f"ID: {student.id}, "
            + f"Name: {student.name}, "
            + f"Email: {student.email}"
        )



def _view_students_by_grade(db):
    say(INDENT + "Students by Grade", GREEN)

    students = db.load_all()

    if not students:
        say(INDENT + "No students found", YELLOW)
        return

    grade_groups = {
        "HD": [],
        "D": [],
        "C": [],
        "P": [],
        "Z": []
    }

    for student in students:
        average = student.average_mark()

        if average >= 85:
            grade = "HD"
        elif average >= 75:
            grade = "D"
        elif average >= 65:
            grade = "C"
        elif average >= 50:
            grade = "P"
        else:
            grade = "Z"

        grade_groups[grade].append(student)

    for grade, group in grade_groups.items():
        say(INDENT + f"Grade {grade}", YELLOW)

        if not group:
            say(INDENT + "No students")
        else:
            for student in group:
                say(
                    INDENT
                    + f"ID: {student.id}, "
                    + f"Name: {student.name}, "
                    + f"Average Mark: {student.average_mark():.2f}"
                )


def _categorize_students(db):
    say(INDENT + "PASS/FAIL Students", GREEN)

    students = db.load_all()

    if not students:
        say(INDENT + "No students found", YELLOW)
        return

    pass_students = []
    fail_students = []

    for student in students:
        if student.average_mark() >= 50:
            pass_students.append(student)
        else:
            fail_students.append(student)

    say(INDENT + "PASS", YELLOW)

    if not pass_students:
        say(INDENT + "No students")
    else:
        for student in pass_students:
            say(
                INDENT
                + f"ID: {student.id}, "
                + f"Name: {student.name}, "
                + f"Average Mark: {student.average_mark():.2f}"
            )

    say(INDENT + "FAIL", YELLOW)

    if not fail_students:
        say(INDENT + "No students")
    else:
        for student in fail_students:
            say(
                INDENT
                + f"ID: {student.id}, "
                + f"Name: {student.name}, "
                + f"Average Mark: {student.average_mark():.2f}"
            )



def _remove_student(db):
    say(INDENT + "Remove Student", GREEN)

    student_id = ask(INDENT + "Enter student ID: ").strip()

    if not student_id:
        say(INDENT + "Student ID cannot be empty", RED)
        return

    removed = db.remove(student_id)

    if removed:
        say(INDENT + f"Student {student_id} removed successfully", YELLOW)
    else:
        say(INDENT + f"Student {student_id} not found", RED)




def _clear_student_data(db):
    say(INDENT + "Clear Student Data", GREEN)

    confirm = ask(
        INDENT + "Are you sure you want to clear all student data? (y/n): "
    ).strip().lower()

    if confirm == "y":
        db.clear()
        say(INDENT + "All student data has been cleared", YELLOW)

    elif confirm == "n":
        say(INDENT + "Clear data cancelled", YELLOW)

    else:
        say(INDENT + "Invalid choice", RED)