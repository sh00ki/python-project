
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
        if len(self.subjects) == 0:
            return 0

        avg = 0
        for subject in self.subjects:
            avg += subject.grade
        avg /= len(self.subjects)
        return avg