"""
Student:
    name: str
    marks: list[int]

Features:
- fetch all students from the database
- add another yet student to the database
- retrieve the student by NAME. UI/UX issues...
"""

# ==================================================
# Simulated storage
# ==================================================
import curses
from typing import Any

students = {
    1: {
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Hobbies: music",
    },
    2: {
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "John is 23 y.o. Hobbies: football",
    },
}

LAST_ID_CONTEXT = 2


def represent_students():
    for id_, student in students.items():
        print(f"[{id_}] {student['name']}, marks: {student['marks']}")


# ==================================================
# CRUD (Create Read Update Delete)
# ==================================================
def add_student(student: dict) -> dict | None:
    global LAST_ID_CONTEXT

    if len(student) != 2:
        return None
    elif not student.get("name") or not student.get("marks"):
        return None
    else:
        LAST_ID_CONTEXT += 1
        students[LAST_ID_CONTEXT] = student

    return student


def search_student(id_: int) -> dict | None:
    return students.get(id_)


def delete_student(id_: int):
    if search_student(id_):
        del students[id_]
        print(f"Student with id '{id_}' is deleted")
    else:
        print(f"There is student '{id_}' in the storage")


def update_student(id_: int, payload: dict) -> dict:
    students[id_] = payload
    return payload


def update_student_by_field(*, id_: int, value: Any, field: str):
    students[id_][field] = value


def student_details(student: dict) -> None:
    print(f"Detailed info: [{student['name']}]...")


# ==================================================
# Handle user input
# ==================================================
def parse(data: str) -> tuple[str, list[int]]:
    """Return student name and marks.

    user input template:
    'John Doe;4,5,4,5,4,5'


    def foo(*args, **kwargs):
        pass

    """

    template = "John Doe;4,5,4,5,4,5"

    items = data.split(";")

    if len(items) != 2:
        raise Exception(f"Incorrect data. Template: {template}")

    # items == ["John Doe", "4,5...."]
    name, raw_marks = items

    if (validate_marks(raw_marks) and validate_name(name)):
        marks = [int(item) for item in raw_marks.split(",")]
    else:
        raise Exception(f"Marks are incorrect. Template: {
                        template}")

    return name, marks


def validate_marks(raw_marks) -> bool:
    try:
        marks = [int(item) for item in raw_marks.split(",")]
        return all(1 <= mark <= 5 for mark in marks)
    except ValueError as error:
        print(error)
        return False


def validate_name(student_full_name: str) -> bool:
    if len(student_full_name.split(' ')) == 2:
        return True
    return False


def ask_student_payload():
    """
    Input template:
        'John Doe;4,5,4,5,4,5'

    Expected:
        John Doe:       str
        4,5,4,5,4,5:    list[int]
    """

    prompt = "Enter student's payload using next template:\n'John Doe;4,5,4,5,4,5': "

    if not (payload := parse(input(prompt))):
        return None
    else:
        name, marks = payload

    return {"name": name, "marks": marks}


def handle_change():
    CHANGE_COMMANDS = {
        "1": "full update",
        "2": "update name",
        "3": "update marks",
        "4": "add marks"
    }
    update_id = input("Enter student's id you wanna change: ")

    try:
        id_ = int(update_id)
    except ValueError as error:
        raise Exception(
            f"ID '{update_id}' is not correct value") from error
    else:
        student = search_student(id_)
        if not student:
            print(f"❌ There is no student with Id: {id_}")
            return
        print("Choose what you want to change.")
        for key, action in CHANGE_COMMANDS.items():
            print(f"{key}: {action.capitalize()}")

        change_action = CHANGE_COMMANDS.get(
            input("Enter the number of action:"))

        if change_action == "full update":
            if data := ask_student_payload():
                update_student(id_, data)
                print(f"✅ Student is updated")
                student_details(student)
        elif change_action == "update name":
            new_name = input(
                "Enter a new name. Using next template:\n'John Doe':")
            if validate_name(new_name):
                update_student_by_field(id_=id_, value=new_name, field='name')
                student_details(student)
            else:
                print(f"❌ Can not change user's name to {
                      new_name}\nPlease enter the correct name")
        elif change_action == "update marks":
            new_marks = input(
                "Enter a new marks. Using next template:\n'2,4,6,7,4':")
            if validate_marks(new_marks):
                update_student_by_field(
                    id_=id_, value=[int(item) for item in new_marks.split(",")], field='marks')
                student_details(student)
            else:
                print(f"❌ Can not change user's marks to {
                      new_marks}\nPlease enter the correct marks")
        elif change_action == "add marks":
            new_marks = input(
                "Enter a new marks. Using next template:\n'2,4,6,7,4':")
            if validate_marks(new_marks):
                united_marks = student["marks"] + \
                    [int(item) for item in new_marks.split(",")]
                update_student_by_field(
                    id_=id_, value=united_marks, field='marks')
                student_details(student)
            else:
                print(f"❌ Can not add new marks {
                      new_marks}\nPlease enter the correct marks")


def handle_management_command(command: str):
    if command == "show":
        represent_students()

    elif command == "retrieve":
        search_id = input("Enter student's id to retrieve: ")

        try:
            id_ = int(search_id)
        except ValueError as error:
            raise Exception(
                f"ID '{search_id}' is not correct value") from error
        else:
            if student := search_student(id_):
                student_details(student)
            else:
                print(f"There is not student with id: '{id_}'")

    elif command == "remove":
        delete_id = input("Enter student's id to remove: ")

        try:
            id_ = int(delete_id)
        except ValueError as error:
            raise Exception(
                f"ID '{delete_id}' is not correct value") from error
        else:
            delete_student(id_)

    elif command == "change":
        handle_change()
    elif command == "add":
        data = ask_student_payload()
        if data is None:
            return None
        else:
            if not (student := add_student(data)):
                print(f"❌ Can't create user with data: {data}")
            else:
                print(f"✅ New student '{student['name']}' is created")
    else:
        raise SystemExit(f"Unrecognized command: '{command}'")


def handle_user_input():
    """This is an application entrypoint."""

    SYSTEM_COMMANDS = ("quit", "help")
    MANAGEMENT_COMMANDS = ("show", "add", "retrieve", "remove", "change")
    AVAILABLE_COMMANDS = SYSTEM_COMMANDS + MANAGEMENT_COMMANDS

    help_message = (
        "Welcome to the Journal application. Use the menu to interact with the application.\n"
        f"Available commands: {AVAILABLE_COMMANDS}"
    )

    print(help_message)

    while True:
        command = input("Enter the command: ")

        try:
            if command == "quit":
                print(f"\nThanks for using Journal application. Bye!")
                break
            elif command == "help":
                print(help_message)
            elif command in MANAGEMENT_COMMANDS:
                handle_management_command(command=command)
            else:
                print(f"Unrecognized command '{command}'")
        except Exception as error:
            print(error)


handle_user_input()
