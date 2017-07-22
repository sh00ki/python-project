from teacher import Teacher
import statistics as stats

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

    def print_students_median(self):
        avg_grades = []
        for teacher in self.teachers:
            for student in teacher.students:
                student_avg = teacher.print_students_average()
                avg_grades.append(student_avg)

        avg_grades.sort()
        median = stats.median(avg_grades)

        return median

    def get_excellent_students(self):
        students_avg = []
        for teacher in self.teachers:
            for student in teacher.students:
                student_avg = teacher.print_student_average(student)
                students_avg.append({"name": student.username, "avg": student_avg})

        max_avgs = sorted(students_avg, key=lambda k: k['avg'], reversed=True)[:3]

        return max_avgs

    def get_excellent_students_by_teacher(self):
        students_avg = []
        for teacher in self.teachers:
            for student in teacher.students:
                student_avg = teacher.print_student_average(student)
                students_avg.append({"name": student.username, "teacher": teacher.username, "avg": student_avg})

        max_avgs = sorted(students_avg, key=lambda k: k['avg'], reversed=True)[:3]

        return max_avgs