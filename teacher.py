

class Teacher:

    def __init__(self, username, password): # constractor
        self.username = username
        self.password = password
        self.students = []
        self.permission = 'teacher'
        self.free_time = []

    def add_subject_for_student(self, student_name, subject):
        if not subject:
            print('There is no subject to add.') # this option not in but is very useful for define profsonals
            return

        for student in self.students:
            if student.username == student_name:
                student.subjects.append(subject) # add the subject to student

    def update_grade_for_student(self, student_name, subject_name, grade): # need to found the subject of student for update the grade
        for student in self.students:
            if student.username == student_name:
                for subject in student.subjects:
                    if subject.name == subject_name:
                        subject.update_grade(grade)

    def print_students_grade(self): # print the grade of all students
        for student in self.students:
            print(student.username)
            for subject in student.subjects:
                print(subject.name, ' ', subject.grade, '\n')

    def print_student_grade(self, student_name): # print the grade of student
        for student in self.students:
            if student.username == student_name:
                print(student.username)
                for subject in student.subjects:
                    print(subject.name, ' ', subject.grade, '\n')

    def print_subject_grades(self, subject_name): # print the grade of all students
        for student in self.students:
            print(student.username)
            for subject in student.subjects:
                if subject.name == subject_name:
                    print(subject.name, ': ', subject.grade, '\n')

    def print_students_average_subject_grade(self, subject_name): #average of subject by teacher
        if len(self.students) == 0:
            return 0
        avg = 0
        for student in self.students:
            print(student.username)
            for subject in student.subjects:
                if subject.name == subject_name:
                    avg += subject.grade
        avg /= len(self.students)
        print('Subject Average is: ', avg, 'for teacher ', self.username, '\n')

    def print_student_average(self, student): # average of student
        if len(student.subjects) == 0:
            return 0

        avg = 0
        for subject in student.subjects:
            avg += subject.grade
        avg /= len(student.subjects)
        return avg

    def print_students_average(self): # average of all students
        if len(self.students) == 0:
            return 0
        avg = 0
        avg_sum = 0
        for student in self.students:
            for subject in student.subjects:
                avg += subject.grade
            if len(student.subjects) != 0:
                avg /= len(student.subjects)
                avg_sum += avg
            avg = 0
        avg_sum /= len(self.students)
        return avg_sum
