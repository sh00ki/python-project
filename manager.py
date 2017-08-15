#from teacher import Teacher
import statistics as stats

class Manager:

    def __init__(self, username, password):  # constractor
        self.username = username
        self.password = password
        self.teachers = []
        self.permission = 'manager'

    def add_teacher(self, teacher): # add teacher to list
        self.teachers.append(teacher)

    def update_teacher(self, teacher_name, new_username): # update the name of teacher
        for teacher in self.teachers:
            if teacher.username == teacher_name: # if found the name
                teacher.username = new_username
                return
        print("Teacher not in list, cant change the name")

    def remove_teacher(self, teacher_name): # remove teacher
        for r in self.teachers:
            if r.username == teacher_name: # if found the teacher
                self.teachers.remove(r) # remove the teacher
                return
        print("Teacher not in list, cant remove the name")


    def add_student_for_teacher(self, teacher_name, student): # add student to teacher
        for teacher in self.teachers:
            if teacher.username == teacher_name: #found the teacher
                teacher.students.append(student) # add the teacher

    def remove_student_from_teacher(self, student_name, teacher_name):
        for r in self.teachers: # looking for teacher in list
            if r.username == teacher_name:
                for a in r.students: # looking for student in teacher list
                    if a.username == student_name:
                        r.students.remove(a)
                    return True
        return False

    def print_students_median(self): # found the median
        avg_grades = []
        median=0
        for teacher in self.teachers:
            for student in teacher.students:
                student_avg = teacher.print_students_average()
                avg_grades.append(student_avg)

        avg_grades.sort() # sort for found the median of al student
        if len(avg_grades) != 0:
            median = stats.median(avg_grades)
        return median

    def get_excellent_students(self): # found the excellent student
        students_avg = [] # list of all student
        for teacher in self.teachers:
            for student in teacher.students:
                student_avg = teacher.print_student_average(student)
                students_avg.append({"name": student.username, "avg": student_avg})

        max_avgs = sorted(students_avg, key=lambda k: k['avg'], reverse=True) # sort from max to min by average
        return max_avgs

    def get_excellent_students_by_teacher(self):
        students_avg = []
        for teacher in self.teachers:
            for student in teacher.students:
                student_avg = teacher.print_student_average(student)
                students_avg.append({"name": student.username, "teacher": teacher.username, "avg": student_avg})

        max_avgs = sorted(students_avg, key=lambda k: k['avg'], reverse=True) # sort from max to min by average
        return max_avgs # this take the max average of 1 teacher - it can be take a more by return more value or change the sorted function to
    #sorted(students_avg, key=lambda k: k['avg'], reverse=True)[:3]  - it take the 3 excellent teachers