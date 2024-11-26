import textwrap

COMMANDS = ("quit", "show", "retrieve", "add")

# Simulated database
students = [
    {
        "id": 0,
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Hobbies: music"
    },
    {
        "id": 1,
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "John is 23 y.o. Hobbies: football"
    }
]


def find_student(*, value: str, key: str = "name") -> dict | None:
    return next((student for student in students if student.get(key) == value), None)


def show_students() -> None:
    print("=" * 20)

    print("The list of students:\n")
    print(
        *[f"{student.get('name')}. Marks:{student['marks']
                                          }" for student in students],
        sep="\n"
    )

    print("=" * 20)


def show_student(*, value: str, key: str = "name") -> None:
    student: dict | None = find_student(value=value, key=key)
    if student:
        print_student_info(student)
    else:
        print(f"There is no student with {key} = {value}")


def print_student_info(student: dict) -> None:
    print("Detailed about student:\n")
    print(
        f"{student['name']}. Marks: {student['marks']}\n"
        f"Details: {textwrap.fill(student['info'], width=50)}\n"
    )


def add_student(student_name: str, details: str | None):
    instance = {"name": student_name, "marks": [], "info": details}
    students.append(instance)

    return instance


def retrieve_handle():
    allowed_keys = ("id", "name")
    key = input(
        f"Would you like to search for a student by {
            ', '.join(allowed_keys)}?\n"
    )

    if key not in allowed_keys:
        print(f"A student doesn't have a {key} property.\n")
        return

    value = input(f"Enter student {key} you are looking for: ")

    if key == "id":
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Invalid input. ID should be a number.")

    show_student(value=value, key=key)


def add_handle():
    student_name = input("Enter student's name: ")
    if not student_name:
        raise Exception(
            "The Name field is required during adding a new Student")

    add_student(
        student_name,
        input("Enter student's details: ")
    )


def main():
    print(f"Welcome to the Digital journal!\nAvailable commands: {COMMANDS}")
    while True:
        user_input = input("Enter the command: ")

        if user_input not in COMMANDS:
            print(f"Command {user_input} is not available.\n")
            continue

        if user_input == "quit":
            print("See you next time.")
            break

        try:
            if user_input == "show":
                show_students()
            elif user_input == "retrieve":
                retrieve_handle()
            elif user_input == "add":
                add_handle()
        except NotImplementedError as error:
            print(f"Feature '{error}' is not ready for live.")
        except Exception as error:
            print(error)


main()
