
class Student:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.subjects = []
        self.permission = 'student'

    def watch_grades(self):
        for subject in self.subjects:
            print(subject.name, ' ', subject.grade, '\n')


    def print_student_average_grades(self):
        avg = 0
        for subject in self.subjects:
            avg += subject.grade
        avg = avg / len(self.subjects)
        return avg