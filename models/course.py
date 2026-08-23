class Course:

    def __init__(self, course_id, title, teacher_id):
        self.course_id = course_id
        self.title = title
        self.teacher_id = teacher_id
        self.enrolled_students = []


    @property
    def get_enrolled_students(self):
        if self.enrolled_students:
            return self.enrolled_students


    def add_student(self, student_id):
        """Method for add specific student to enrolled_students list in Course"""
        if len(self.enrolled_students) < 25:
            if student_id not in self.enrolled_students:
                self.enrolled_students.append(student_id)
            else:
                raise ValueError("Student is already registered")
        else:
            raise ValueError("Course reached its maximum student capacity of 25")


    def remove_student(self, student_id):
        """Method for remove specific student from enrolled_students list in Course"""
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
        else:
            raise ValueError("No student is registered in this course")