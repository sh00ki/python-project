
class Student:

    def __init__(self, username, password):  # constractor
        self.username = username
        self.password = password
        self.subjects = []
        self.permission = 'student'

    def watch_grades(self): # watch the grades of student
        for subject in self.subjects:
            print(subject.name, ' ', subject.grade, '\n')

    def print_student_average_grades(self): #average of student
        if len(self.subjects) == 0:
            return 0

        avg = 0
        for subject in self.subjects: # sum the all grades of subject
            avg += subject.grade
        avg /= len(self.subjects) #do to average
        return avg # reutrn the average