# School Management System

A Python command-line application for managing students, teachers, and courses in a school. The project applies object-oriented programming, JSON file handling, input validation, exception handling, and error logging.

## Features

- Add, remove, and display students
- Add, remove, and display teachers
- Add, remove, and display courses
- Enroll and unenroll students in courses
- View a student's enrolled courses
- View students enrolled in a course
- Assign courses to teachers
- Validate user input and IDs
- Save and restore data using JSON files
- Log application errors to a text file

## Project Structure

school_system/
- main.py
- models/
  - school.py
  - student.py
  - course.py
  - teacher.py
- utils/
  - validators.py
  - file_handler.py
  - logging_handler.py
- data/
  - students.json
  - courses.json
  - teachers.json
- log.txt
- Project_Unit2_Documentation.pdf
- Project_Unit2_Diagrams.drawio

## Main Classes

**School**  
Coordinates students, courses, and teachers and manages the relationships between them.

**Student**  
Stores student information and enrolled course IDs.

**Course**  
Stores course information, the assigned teacher, and enrolled student IDs.

**Teacher**  
Stores teacher information and assigned course IDs.

## Business Rules

- A student can enroll in a maximum of 7 courses.
- A course can contain a maximum of 25 students.
- A teacher can be assigned to a maximum of 6 courses.
- Duplicate course enrollment is not allowed.
- A teacher cannot be deleted while assigned to courses.

## Data Persistence

The application stores its records in three JSON files:

- `data/students.json`
- `data/courses.json`
- `data/teachers.json`

Saved records are loaded when the program starts. Changes are written back to the JSON files during the program and when the user selects **Save and Exit**.

## Validation and Logging

Input validation is handled in `utils/validators.py`. Invalid values raise exceptions with clear messages.

Errors caught by the main program are recorded in `log.txt` through `utils/logging_handler.py`.

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the project root directory.
3. Run:

`python main.py`

4. Follow the numbered menu displayed in the terminal.

## UML Design

The project includes the following UML diagrams:

- Class Diagram
- Use Case Diagram
- Activity Diagram for student course enrollment

The editable diagrams are available in:

`Project_Unit2_Diagrams.drawio`

## Documentation

Full project documentation is available in:

`Project_Unit2_Documentation.pdf`

## Author

**Ghadah Ammar Alabbadi**

Unit 2 Project - School Management System
