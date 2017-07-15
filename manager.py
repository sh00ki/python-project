from teacher import Teacher

class Manager:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.teachers = []
        self.permission = 'manager'

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_teachers(self, teachers):
        self.teachers = teachers

    def update_teacher(self, teacher_name, new_username):
        for teacher in self.teachers:
            if teacher.username == teacher_name:
                teacher.username = new_username

    def remove_teacher(self, teacher_name):
        for r in self.teachers:
            # for d in r.items():
            if r.username == teacher_name:
                self.teachers.remove(r)
                pass


        # for teacher in self.teachers:
        #     if teacher.username == teacher_name:
        #         self.teachers.remove(teacher_name)

    def add_student_for_teacher(self, teacher_name, student):
        for teacher in self.teachers:
            if teacher.username == teacher_name:
                teacher.students.append(student)

    def add_students_for_teacher(self, teacher_name, students):
        for teacher in self.teachers:
            if teacher.username == teacher_name:
                teacher.students = students

    def remove_student_from_teacher(self, student_name, teacher_name):
        for r in self.teachers:
            if r.username == teacher_name:
                for a in r.students:
                    # for d in r.items():
                    if a.username == student_name:
                        r.students.remove(a)
                    pass
                    # for teacher in self.teachers:
                    #     if teacher.username == teacher_name:
                    #         for student in teacher.students:
                    #             if student.username == student_name:
                    #                 teacher.students.remove(student_name)

    def remove_subject_from_student(self, teacher_name, student_name, subject_name):
        for teacher in self.teachers:
            if teacher.username == teacher_name:
                for student in teacher.students:
                    if student.username == student_name:
                        for subject in student.subjects:
                            if subject.name == subject_name:
                                student.subjects.remove(subject_name)