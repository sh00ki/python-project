
class Subject:

    def __init__(self, name, grade):  # constractor
        self.name = name
        self.grade = grade

    def update_grade(self, grade): # update the grade of student by teacher
        self.grade = grade
