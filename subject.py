
class Subject:

    def __init__(self, name, grade):
        self.name = name
        self.grade = int(grade) if grade else 0 #TODO - Chcek if grade is between 0-100

    def update_grade(self, grade):
        self.grade = grade  #TODO - Chcek if grade is between 0-100