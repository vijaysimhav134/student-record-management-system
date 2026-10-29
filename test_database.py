
import unittest
import sqlite3
import tempfile
import os
from unittest.mock import patch

import database


class TestStudentDatabase(unittest.TestCase):

    def setUp(self):
        # Create a temporary database for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.connection = sqlite3.connect(self.temp_file.name)
        self.connection.execute("""
            CREATE TABLE students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT
            )
        """)
        self.connection.commit()
        self.connection.close()

        # Redirect database operations to the temporary database
        self.db_patcher = patch.object(
            database, "DB_NAME", self.temp_file.name
        )
        self.db_patcher.start()

    def tearDown(self):
        self.db_patcher.stop()
        os.remove(self.temp_file.name)

    def test_add_and_search_student(self):
        database.add_student("Vijay", 22, "ECE")

        student = database.search_student(1)

        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Vijay")
        self.assertEqual(student[2], 22)
        self.assertEqual(student[3], "ECE")

    def test_view_students(self):
        database.add_student("Simha", 21, "CSE")

        students = database.view_students()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0][1], "Simha")

    def test_delete_student(self):
        database.add_student("Vijay", 22, "ECE")

        result = database.delete_student(1)

        self.assertTrue(result)
        self.assertIsNone(database.search_student(1))

    def test_update_student(self):
        database.add_student("Vijay", 22, "ECE")

        result = database.update_student(1, "Vijay", 23, "CSE")
        student = database.search_student(1)

        self.assertTrue(result)
        self.assertEqual(student[2], 23)
        self.assertEqual(student[3], "CSE")

    def test_search_missing_student(self):
        student = database.search_student(999)

        self.assertIsNone(student)


if __name__ == "__main__":
    unittest.main()
