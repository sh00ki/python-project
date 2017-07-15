
class Student:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.subjects = []
        self.permission = 'student'

    def watch_grades(self):
        for subject in self.subjects:
            print(subject.name, ' ', subject.grade, '\n')