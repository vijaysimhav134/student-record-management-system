# Student Record Management System

A command-line application built using Python and SQLite to manage student records. The project demonstrates CRUD operations, input validation, database integration, and automated unit testing.

## Features

- Add student records
- View all student records
- Search students by ID
- Update student details
- Delete student records
- Validate user input
- Store records persistently using SQLite
- Automated unit tests for database operations

## Technologies Used

- Python 3
- SQLite
- SQL
- `unittest`
- Git and GitHub

## Project Structure

```text
StudentRecordSystem/
├── main.py
├── database.py
├── test_database.py
├── README.md
└── .gitignore
```

The SQLite database file is created locally when the application runs and is excluded from the public repository.

## Requirements

- Python 3 installed
- No additional Python packages required

## Run the Application

Open a terminal in the project directory and run:

```bash
python3 main.py
```

On Windows, you can also use `python main.py` if that command is configured on your system.

## Run Automated Tests

Execute:

```bash
python3 -m unittest -v test_database.py
```

The tests verify adding, viewing, searching, updating, and deleting student records using a temporary database.

## Database Operations

The application implements CRUD operations:

- **Create:** Add a student record.
- **Read:** View all records or search by student ID.
- **Update:** Modify an existing student's details.
- **Delete:** Remove a student record.

## Learning Outcomes

- Writing reusable Python functions
- Working with SQL queries and SQLite
- Handling invalid user input
- Separating application logic from database logic
- Writing automated unit tests
- Managing source code with GitHub
