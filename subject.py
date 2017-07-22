
class Subject:

    def __init__(self, name, grade):  # constractor
        self.name = name
        if grade.isdigit() and grade>=0 and grade<=100:
            self.grade = int(grade) if grade else 0

    def update_grade(self, grade):
        if  grade.isdigit()and grade >= 0 and grade <= 100:
            self.grade = grade