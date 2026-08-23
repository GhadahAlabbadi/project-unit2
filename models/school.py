class School:

    def __init__(self):
        self.students = {}
        self.courses = {}
        self.teachers = {}

    #----------RELATED TO STUDENT----------#
    @property
    def get_students(self):
        return self.students


    def search_student_by_id(self, student_id):
        """Method for searching specific student in students dict in School"""
        if not self.students:
            raise ValueError("\nThere are no students currently")
        if student_id in self.students:
            return self.students[student_id]
        raise ValueError("\nNo student with this ID")


    def add_student(self, student):
        """Method for add specific student object to students dict in School"""
        self.students[student.student_id] = student

    
    def drop_student(self, student_id):
        """Method for delete specific student object from students dict in School"""
        for course in self.courses.values():
            if student_id in course.enrolled_students:
                course.remove_student(student_id)
        self.students.pop(student_id)


    def enroll_student(self, student_id, course_id):
        """Method for enroll specific student to specific course in School"""
        student = self.search_student_by_id(student_id)
        course = self.search_course_by_id(course_id)
        if len(course.enrolled_students) >= 25:
            raise ValueError("Course reached its maximum student capacity of 25")
        student.enroll_to_course(course_id)
        course.add_student(student_id)


    def unenroll_student(self, student_id, course_id):
        """Method for unenroll specific student from specific course in School"""
        student = self.search_student_by_id(student_id)
        course = self.search_course_by_id(course_id)
        student.unenroll_to_course(course_id)
        course.remove_student(student_id)

        
    def display_students(self):
        if self.students:
            print("\n" + "=" * 50)
            print("STUDENTS")
            print("=" * 50)
            for student in self.students.values():
                courses = (", ".join(student.enrolled_courses) if student.enrolled_courses else "No courses enrolled")
                print(f"ID: {student.student_id}\nName: {student.name}\nAge: {student.age}\nCourses: {courses}\n" + "-" * 50)
        else:
            print("\nThere are no students currently")

    #----------RELATED TO COURSE----------#
    @property
    def get_courses(self):
        return self.courses


    def search_course_by_id(self, course_id):
        """Method for searching specific course in courses dict in School"""
        if not self.courses:
            raise ValueError("\nThere are no courses currently")
        if course_id in self.courses:
            return self.courses[course_id]
        raise ValueError("\nNo course with this ID")

       
    def add_course(self, course):
        """Method for add specific course object to courses dict in School"""
        self.courses[course.course_id] = course


    def delete_course(self, course_id):
        """Method for delete specific course from courses dict in School"""
        for student in self.students.values():
            if course_id in student.enrolled_courses:
                student.unenroll_to_course(course_id)
        self.courses.pop(course_id)

             
    def display_courses(self):
        if self.courses:
            print("\n" + "=" * 50)
            print("COURSES")
            print("=" * 50)
            for course in self.courses.values():
                students = (", ".join(course.enrolled_students) if course.enrolled_students else "No students enrolled")
                print(f"ID: {course.course_id}\nTitle: {course.title}\nTeacher: {course.teacher_id}\nStudents: {students}\n" + "-" * 50)
        else:
            print("\nThere are no courses currently")

    #----------RELATED TO TEACHER----------#
    @property
    def get_teachers(self):
        return self.teachers


    def search_teacher_by_id(self, teacher_id):
        """Method for searching specific teacher in teachers dict in School"""
        if not self.teachers:
            raise ValueError("\nThere are no teachers currently")
        if teacher_id in self.teachers:
            return self.teachers[teacher_id]
        raise ValueError("\nNo teacher with this ID")


    def add_teacher(self, teacher):
        """Method for add specific teacher object to teachers dict in School"""
        self.teachers[teacher.teacher_id] = teacher


    def drop_teacher(self, teacher_id):
        """Method for delete specific teacher from teachers dict in School"""
        teacher = self.search_teacher_by_id(teacher_id)
        if teacher.subjects:
            raise ValueError("Teacher can't be deleted while assigned to courses")
        self.teachers.pop(teacher_id)


    def assign_subjects(self, teacher_id, course_id):
        """Method for assign specific teacher to specific course in School"""
        self.teachers[teacher_id].add_subject(course_id)


    def delete_subject(self, teacher_id, course_id):
        """Method for unassign specific teacher from specific course in School"""
        self.teachers[teacher_id].drop_subject(course_id)

        
    def display_teachers(self):
        if self.teachers:
            print("\n" + "=" * 50)
            print("TEACHERS")
            print("=" * 50)
            for teacher in self.teachers.values():
                subjects = (", ".join(teacher.subjects) if teacher.subjects else "No courses assigned")
                print(f"ID: {teacher.teacher_id}\nName: {teacher.name}\nSubjects: {subjects}\n" + "-" * 50)
        else:
            print("\nThere are no teachers currently")