class Teacher:

    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.subjects = []


    def add_subject(self, subject):
        """Method for add specific subject to teacher in Teacher"""
        if len(self.subjects) < 6:
            self.subjects.append(subject)
        else:
            raise ValueError("Teacher reached the maximum number of courses")


    def drop_subject(self, subject):
        """Method for delete specific subject from teacher in Teacher"""
        if subject in self.subjects:
            self.subjects.remove(subject)