
class Teacher:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.students = []
        self.permission = 'teacher'
        self.free_time = []

    def add_subject_for_student(self, student_name, subject):
        if not subject:
            print('There is no subject to add.')
            return

        for student in self.students:
            if student.username == student_name:
                student.subjects.append(subject)

    def update_grade_for_student(self, student_name, subject_name, grade):
        for student in self.students:
            if student.username == student_name:
                for subject in student.subjects:
                    if subject.name == subject_name:
                        subject.update_grade(grade)

    def print_students_grade(self):
        for student in self.students:
            print(student.username)
            for subject in student.subjects:
                print(subject.name, ' ', subject.grade, '\n')

    def print_student_grade(self, student_name):
        for student in self.students:
            if student.username == student_name:
                print(student.username)
                for subject in student.subjects:
                    print(subject.name, ' ', subject.grade, '\n')

    def print_subject_grades(self, subject_name):
        for student in self.students:
            print(student.username)
            for subject in student.subjects:
                if subject.name == subject_name:
                    print(subject.name, ': ', subject.grade, '\n')

    def print_students_average_subject_grade(self, subject_name):
        avg = 0
        for student in self.students:
            print(student.username)
            for subject in student.subjects:
                if subject.name == subject_name:
                    avg += subject.grade
        avg = avg / len(self.students)
        print('Subject Average is: ', avg, 'for teacher ', self.username, '\n')

