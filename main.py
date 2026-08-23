from models import student as st, course as crs, teacher as tch, school 
from utils import validators as vd
from utils import file_handler, logging_handler


STUDENTS_FILE = "data/students.json"
COURSES_FILE = "data/courses.json"
TEACHERS_FILE = "data/teachers.json"
SCHOOL_OBJECT = school.School()


def load_students():
    students_dict = file_handler.read_json(STUDENTS_FILE)
    for student_id, data in students_dict.items():
        student = st.Student(student_id, data["name"], data["age"])
        student.enrolled_courses = data.get("enrolled_courses", [])
        SCHOOL_OBJECT.add_student(student)


def load_teachers():
    teachers_dict = file_handler.read_json(TEACHERS_FILE)
    for teacher_id, data in teachers_dict.items():
        teacher = tch.Teacher(teacher_id, data["name"])
        teacher.subjects = data.get("subjects", [])
        SCHOOL_OBJECT.add_teacher(teacher)


def load_courses():
    courses_dict = file_handler.read_json(COURSES_FILE)
    for course_id, data in courses_dict.items():
        course = crs.Course(course_id, data["title"], data["teacher_id"])
        course.enrolled_students = data.get("enrolled_students", [])
        SCHOOL_OBJECT.add_course(course)


def save_changes_students():
    students_dict = {}
    for student_id, student in SCHOOL_OBJECT.get_students.items():
        students_dict[student_id] = {"student_id": student.student_id,
                                     "name": student.name,
                                     "age": student.age,
                                     "enrolled_courses": student.enrolled_courses}
    file_handler.write_to_json(STUDENTS_FILE, students_dict)


def save_changes_teachers():
    teachers_dict = {}
    for teacher_id, teacher in SCHOOL_OBJECT.get_teachers.items():
        teachers_dict[teacher_id] = {"teacher_id": teacher.teacher_id,
                                     "name": teacher.name,
                                     "subjects": teacher.subjects}
    file_handler.write_to_json(TEACHERS_FILE, teachers_dict)


def save_changes_courses():
    courses_dict = {}
    for course_id, course in SCHOOL_OBJECT.get_courses.items():
        courses_dict[course_id] = {"course_id": course.course_id,
                                    "title": course.title,
                                    "teacher_id": course.teacher_id,
                                    "enrolled_students": course.enrolled_students}
    file_handler.write_to_json(COURSES_FILE, courses_dict)


def generate_ids(object_type, title= ""):
    """Function for generate IDs to all users"""
    generated_id = ""
    if object_type == "student":
        students_dict = SCHOOL_OBJECT.get_students
        if students_dict:
            last_id = list(students_dict.keys())[-1]
            splited_list = last_id.split("-")
            number = str(int(splited_list[1]) + 1)
            generated_id = splited_list[0] + "-" + number
            return generated_id
        else:
            generated_id = "S0-1"
            return generated_id
    elif object_type == "course":
        courses_dict = SCHOOL_OBJECT.get_courses
        prefix = title.strip()[:3].upper()
        if courses_dict:
            last_id = list(courses_dict.keys())[-1]
            splited_list = last_id.split("-")
            number = str(int(splited_list[1]) + 1)
            generated_id = prefix + "-" + number
            return generated_id
        return prefix + "-1"
    elif object_type == "teacher":
        teachers_dict = SCHOOL_OBJECT.get_teachers
        if teachers_dict:
            last_id = list(teachers_dict.keys())[-1]
            splited_list = last_id.split("-")
            number = str(int(splited_list[1]) + 1)
            generated_id = splited_list[0] + "-" + number
            return generated_id
        else:
            generated_id = "T0-1"
            return generated_id
    else:
        return "ID cannot be created"


def display_menu():
    """Function for print the menu"""
    print("""
============================================================
                 SCHOOL MANAGEMENT SYSTEM
============================================================

[ STUDENT MANAGEMENT ]
  1. Add Student
  2. Delete Student
  3. Enroll Student in Course
  4. Unenroll Student from Course
  5. View Student Courses
  6. View All Students

[ TEACHER MANAGEMENT ]
  7. Add Teacher
  8. Delete Teacher
  9. View All Teachers

[ COURSE MANAGEMENT ]
 10. Add Course
 11. Delete Course
 12. View Course Students
 13. View All Courses

------------------------------------------------------------
  0. Save and Exit
============================================================""")


def print_success(message):
    print(f"\n[SUCCESS] {message}")


def print_error(message):
    print(f"\n[ERROR] {message}")


load_students()
load_teachers()
load_courses()


while True:

    display_menu()

    try:
        user_choice = input("Choose an option: ")
        match user_choice:
            case "1":
                name = vd.validate_string(input("Enter student name: "))
                age = vd.validate_number(input("Enter student age: "))
                if name and age:
                    student_id = generate_ids("student")
                    student = st.Student(student_id, name, age)
                    SCHOOL_OBJECT.add_student(student)
                    save_changes_students()
                    print_success(f"Student {student_id} - {student.name} was added successfully.")
            case "2":
                SCHOOL_OBJECT.display_students()
                if SCHOOL_OBJECT.get_students:
                    student_id = vd.validate_student_id(input("\nEnter student ID: "))
                    SCHOOL_OBJECT.drop_student(student_id)
                    save_changes_students()
                    save_changes_courses()
                    print_success(f"Student {student_id} was deleted successfully.")
            case "3":
                if SCHOOL_OBJECT.get_courses:
                    SCHOOL_OBJECT.display_students()
                    student_id = vd.validate_student_id(input("\nEnter student ID: "))
                    if student_id:
                        SCHOOL_OBJECT.display_courses()
                        course_id = vd.validate_course_id(input("\nEnter course ID: "))
                        if course_id:
                            SCHOOL_OBJECT.enroll_student(student_id, course_id)
                            save_changes_students()
                            save_changes_courses()
                            print_success(f"Student {student_id} was enrolled in course {course_id}.")
                        else:
                            raise ValueError("Course ID not correct")
                    else:
                        raise ValueError("Student ID not correct") 
                else:
                    print("\nThere are no courses currently")          
            case "4":
                SCHOOL_OBJECT.display_students()
                if SCHOOL_OBJECT.get_students:
                    student_id = vd.validate_student_id(input("\nEnter student ID: "))
                    student = SCHOOL_OBJECT.search_student_by_id(student_id)
                    if student.get_enrolled_courses:
                        courses = ", ".join(student.get_enrolled_courses)
                        print(f"\nEnrolled Courses: {courses}")
                        course_id = vd.validate_course_id(input("Enter course ID: "))
                        if course_id in student.get_enrolled_courses:
                            SCHOOL_OBJECT.unenroll_student(student_id, course_id)
                            save_changes_students()
                            save_changes_courses()
                            print_success(f"Student {student_id} was unenrolled from course {course_id}.")
                        else:
                            raise ValueError("Course not available to this student")
                    else:
                        print("\nStudent not enrolled in any courses")
            case "5":
                SCHOOL_OBJECT.display_students()
                if SCHOOL_OBJECT.get_students:
                    student_id = vd.validate_student_id(input("\nEnter student ID: "))
                    student = SCHOOL_OBJECT.search_student_by_id(student_id)
                    if student.get_enrolled_courses:
                        courses = ", ".join(student.get_enrolled_courses)
                        print("\n" + "=" * 60)
                        print("                 STUDENT COURSES")
                        print("=" * 60)
                        print(f"Student ID : {student.student_id}")
                        print(f"Name       : {student.name}")
                        print(f"Courses    : {courses}")
                        print("=" * 60)
                    else:
                        print("Student not enrolled in any courses")
            case "6":
                SCHOOL_OBJECT.display_students()
            case "7":
                name = vd.validate_string(input("Enter teacher name: "))
                if name:
                    teacher_id = generate_ids("teacher")
                    teacher = tch.Teacher(teacher_id, name)
                    SCHOOL_OBJECT.add_teacher(teacher)
                    save_changes_teachers()
                    print_success(f"Teacher {teacher_id} was added successfully.")
            case "8":
                SCHOOL_OBJECT.display_teachers()
                if SCHOOL_OBJECT.get_teachers:
                    teacher_id = vd.validate_teacher_id(input("\nEnter teacher ID: "))
                    if teacher_id:
                        SCHOOL_OBJECT.drop_teacher(teacher_id)
                        save_changes_teachers()
                        save_changes_courses()
                        print_success(f"Teacher {teacher_id} was deleted successfully.")
            case "9":
                SCHOOL_OBJECT.display_teachers()
            case "10":
                if SCHOOL_OBJECT.get_teachers:
                    title = vd.validate_string(input("Enter course title: "))
                    title = vd.validate_duplicate_courses(title)
                    if title:
                        SCHOOL_OBJECT.display_teachers()
                        teacher_id = vd.validate_teacher_id(input("\nEnter teacher ID: "))
                        if teacher_id:
                            course_id = generate_ids("course", title)
                            course = crs.Course(course_id, title, teacher_id)
                            SCHOOL_OBJECT.assign_subjects(teacher_id, course_id)
                            SCHOOL_OBJECT.add_course(course)
                            save_changes_courses()
                            save_changes_teachers()
                            print_success(f"Course {course_id} - {title} was added successfully.")
                else:
                    print("\nThere are no teachers currently")
            case "11":
                SCHOOL_OBJECT.display_courses()
                if SCHOOL_OBJECT.get_courses:
                    course_id = vd.validate_course_id(input("\nEnter course ID: "))
                    if course_id:
                        course = SCHOOL_OBJECT.search_course_by_id(course_id)
                        SCHOOL_OBJECT.delete_course(course_id)
                        SCHOOL_OBJECT.delete_subject(course.teacher_id, course_id)
                        save_changes_courses()
                        save_changes_students()
                        save_changes_teachers()
                        print_success(f"Course {course_id} - {course.title} was deleted successfully.")
            case "12":
                SCHOOL_OBJECT.display_courses()
                if SCHOOL_OBJECT.get_courses:
                    course_id = vd.validate_course_id(input("\nEnter course ID: "))
                    if course_id:
                        course = SCHOOL_OBJECT.search_course_by_id(course_id)
                        if course.get_enrolled_students:
                            print("\n" + "=" * 60)
                            print("                 COURSE STUDENTS")
                            print("=" * 60)
                            print(f"Course ID : {course.course_id}")
                            print(f"Title     : {course.title}")
                            print("Students  :")
                            for student_id in course.get_enrolled_students:
                                student = SCHOOL_OBJECT.search_student_by_id(
                                    student_id
                                )
                                print(f"  - {student_id} | {student.name}")
                            print("=" * 60)
                        else:
                            print("No students in this course")
            case "13":
                SCHOOL_OBJECT.display_courses()
            case "0":
                save_changes_students()
                save_changes_courses()
                save_changes_teachers()
                print("THANK YOU!\n")
                break
            case _:
                raise ValueError("Please write valid choice!")
    except Exception as e:
        print_error(str(e))
        logging_handler.log_error(str(e))     