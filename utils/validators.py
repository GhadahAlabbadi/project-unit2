from utils import file_handler


STUDENTS_FILE = "data/students.json"
COURSES_FILE = "data/courses.json"
TEACHERS_FILE = "data/teachers.json"


def validate_string(value):
    """Function for validate String input in validators file"""
    value = " ".join(value.strip().split())
    if not value:
        raise ValueError("Field can't be empty")
    if not value.replace(" ", "").isalpha():
        raise ValueError("Field must contain letters only")
    return value.title()


def validate_number(number):
    """Function for validate Integer input in validators file"""
    number = number.strip()
    if not number:
        raise ValueError("Field can't be empty")
    elif not number.isdigit():
        raise ValueError("Field must be a number")
    elif int(number) < 5 or int(number) > 65:
        raise ValueError("Age must be greater than 4 and less than 66")
    else:
        return int(number)


def validate_student_id(student_id):
    """Function for validate studentId in validators file"""
    student_id = student_id.strip()
    students_dict = file_handler.read_json(STUDENTS_FILE)
    if student_id not in students_dict:
        raise ValueError("No student with this ID")
    else:
        return student_id


def validate_course_id(course_id):
    """Function for validate courseId in validators file"""
    course_id = course_id.strip()
    courses_dict = file_handler.read_json(COURSES_FILE)
    if course_id not in courses_dict:
        raise ValueError("No course with this ID")
    else:
        return course_id


def validate_teacher_id(teacher_id):
    """Function for validate teacherId in validators file"""
    teacher_id = teacher_id.strip()
    teachers_dict = file_handler.read_json(TEACHERS_FILE)
    if teacher_id not in teachers_dict:
        raise ValueError("No teacher with this ID")
    else:
        return teacher_id


def validate_duplicate_courses(title):
    """Function for validate duplicated courses in validators file"""
    flag = True
    courses_dict = file_handler.read_json(COURSES_FILE)
    if courses_dict:
        for course_id, course in courses_dict.items():
            if course["title"] == title:
                flag = False 
        if flag:
            return title
        else:
            raise ValueError("\nCourse already exists")
    else:
        return title