
import database


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter student age: ").strip())

        if age <= 0:
            print("Age must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number for age.")
        return

    course = input("Enter course: ").strip()

    database.add_student(name, age, course)
    print("Student added successfully!")


def view_students():
    students = database.view_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])


def search_student():
    try:
        student_id = int(input("Enter student ID to search: ").strip())
        if student_id <= 0:
            print("ID must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    student = database.search_student(student_id)

    if student:
        print("\nID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
    else:
        print("Student not found.")


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: ").strip())
        if student_id <= 0:
            print("ID must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    if database.delete_student(student_id):
        print("Student deleted successfully!")
    else:
        print("Student not found. Nothing was deleted.")


def update_student():
    try:
        student_id = int(input("Enter student ID to update: ").strip())
        if student_id <= 0:
            print("ID must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    student = database.search_student(student_id)

    if not student:
        print("Student not found.")
        return

    print("\nCurrent details:")
    print("Name:", student[1])
    print("Age:", student[2])
    print("Course:", student[3])

    name = input("Enter new name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter new age: ").strip())

        if age <= 0:
            print("Age must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number for age.")
        return

    course = input("Enter new course: ").strip()

    if database.update_student(student_id, name, age, course):
        print("Student details updated successfully!")
    else:
        print("Student not found.")


def main():
    database.initialize_database()

    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by ID")
        print("4. Delete Student by ID")
        print("5. Update Student Details")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
