
import sqlite3

DB_NAME = "student.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_student(name, age, course):
    connection = get_connection()

    connection.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    connection.commit()
    connection.close()


def view_students():
    connection = get_connection()
    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()
    connection.close()

    return students


def search_student(student_id):
    connection = get_connection()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    connection.close()
    return student


def delete_student(student_id):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()

    return deleted


def update_student(student_id, name, age, course):
    connection = get_connection()

    cursor = connection.execute(
        """UPDATE students
           SET name = ?, age = ?, course = ?
           WHERE id = ?""",
        (name, age, course, student_id)
    )

    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()

    return updated
