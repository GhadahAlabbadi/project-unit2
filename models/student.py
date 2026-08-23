class Student:

    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.enrolled_courses = []


    @property
    def get_enrolled_courses(self):
        return self.enrolled_courses


    def enroll_to_course(self, course_id):
        """Method for enroll student to specific course in Student"""
        if len(self.enrolled_courses) < 7:
            if course_id not in self.enrolled_courses:
                self.enrolled_courses.append(course_id)
            else:
                raise ValueError("Student is already registered for this course")
        else:
            raise ValueError("Student reached the maximum number of course registrations, which is 7")


    def unenroll_to_course(self, course_id):
        """Method for unenroll student from specific course in Student"""
        if course_id in self.enrolled_courses:
            self.enrolled_courses.remove(course_id)
        else:
            raise ValueError("Student not registered for this course")