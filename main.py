from student import Student
from teacher import Teacher
from manager import Manager
from subject import Subject
import random
import csv
import xlsxwriter # use this for write the excel file

managers_list = []
teachers_list = []
students_list = []
flag_admin = False


def main_options(): # the main options
    while (True):
        print("Please choose one of options:\n")
        print('1. Login as Manager\n') #only admin can enter - User:Yoad, password:1234
        print('2. Login as Teacher\n') #only teacher can enter - need to register teachers in admin option
        print('3. Login as Student\n') # only student can enter - need to register students in admin option
        print('4. Quit\n')

        opt = input() # waiting for option
        if opt == '1':
            username = input("What is your username? ") #def - Yoad
            password = input("What is your password? ") #def - 1234
            if manager.username == username and manager.password == password: # validate the username and pasword
                print('Welcome ', manager.username)
                flag_admin = True # bool flag for back the main
                manager_options(flag_admin)

        elif opt == '2':
            username = input("What is your username? ") # need to register teachers in admin option
            password = input("What is your password? ")
            for teacher in manager.teachers: # validate if teachers is exist
                if teacher.username == username and teacher.password == password: # validate the username and password
                    print('Welcome ', teacher.username)
                    flag_teacher = True # bool flag for back the main
                    teacher_options(teacher, flag_teacher)
        elif opt == '3':
            username = input("What is your username? ") # need to register students in admin option
            password = input("What is your password? ")
            for student in students_list: # valide if the students is exist
                if student.username == username and student.password == password: # validate the username and password
                    print('Welcome ', student.username)
                    flag_student = True # bool flag for back the main
                    student_options(student, flag_student)
        elif opt == '4': # stop and exit the program
            exit(0)
        else:
            continue # if the user not enter the number 1,2,3,4


def manager_options(flag_admin): # manager options

    while(flag_admin):
        print("Please choose one of options:\n")
        print("1. Register Teacher\n")
        print("2. Update Teacher\n")
        print("3. Remove Teacher\n")
        print("4. Register Student\n")
        print("5. Remove Student\n")
        print("6. Generate Teachers' Free Time\n")
        print("7. Print Teachers' Free Time\n")
        print("8. Output Report\n")
        print("9. Sign Out\n")
        print("10. Quit")
        option = input()
        if option == "1": # register teacher
            teacher_username = input("Insert teacher username")
            if validate_teacher_exist(teacher_username) is None:
                teacher_password = input("Insert teacher password")
                if not teacher_username.isalpha():
                    print("The username must be a string, not with numbers")
                    continue
                if teacher_username is None or teacher_username == '' or teacher_password is None or teacher_password == '':
                    print("one of values is null, please try again")
                    continue
                if len(teachers_list) <= number_of_teachers:
                    teacher = Teacher(teacher_username, teacher_password) # send to constractor
                    manager.add_teacher(teacher)
                    teachers_list.append(teacher) # append the teacher to list
                else :
                    print("Can't register more teachers to school!")
                print("Done ! new teacher has registered to school")
            else:
                print("the username of this teacher is exist, back to main...")
        elif option == "2":
            teacher_username = input("Insert teacher username")
            if not validate_teacher_exist(teacher_username) is None:
                teacher_new_username = input("Insert teacher new username")
                manager.update_teacher(teacher_username, teacher_new_username) # update the name of the teacher
                print("Done! - the name of teacher was updated!")
            else:
                print("Not found the username of teacher")
        elif option == "3":
            teacher_username = input("Insert teacher username")
            if not manager.remove_teacher(teacher_username): # remove teacher
                continue
            print("Done! - teacher has removed")
            for teacher in teachers_list: # check if the name of teacher exist
                if teacher.name == teacher_username: # if exist remove him
                    teachers_list.remove(teacher) # remove teacher from list
        elif option == "4":
            student_username = input("Insert student username")
            student_password = input("Insert student password")
            if not student_username.isalpha():
                print("The username must be a string, not with numbers")
                continue
            if student_username is None or student_username == '' or student_password is None or student_password == '':
                print("one of values is null, please try again")
                continue
            for r in students_list:
                for d in vars(r).items():
                    if d[0] == student_username: # check if the student is exist
                        print('The student ', student.username, ' was registred.')
                        continue
            if len(students_list) <= number_of_students_per_school: # check if the can register students becuase have max
                print('The student',student_username, 'has added to list')
                teacher_username = input("Insert teacher username")
                teacher = validate_teacher_exist(teacher_username)
                if teacher is not None: # check if the teacher is exist
                    if len(teacher.students) < number_of_students_per_teacher: # every teacher have max students of he/she can teach
                        student = Student(student_username, student_password) # new student - send to constractor
                        manager.add_student_for_teacher(teacher_username, student) # append the student to teacher
                        students_list.append(student) # add student to list of students
                        print("Done - The student ",student_username, "added to teacher: ", teacher_username,"\n")
                    else:
                        print("The teacher ", teacher_username, "is full ! - cant register more students to this teacher")
                else:
                    print("The student ", student_username, " was deleted because he doesn't have teacher")
            else:
                print("The school is full students, can't register more students")

        elif option == "5":
            student_username = input("Insert student username")
            teacher_username = input("Insert teacher username")
            if  not manager.remove_student_from_teacher(student_username, teacher_username): # remove the student from teachr of he/she study with him
                print ("Have some problem - cant remove the student")
                continue
            for student in students_list: # looking for the student
                if student.username == student_username:
                    students_list.remove(student) # remove the student from list
        elif option == "6":
            generate_free_time() #buliding board for study
        elif option == "7":
            print_teachers_free_time() # found the free time in board
        elif option == "8":
            export_xlsx_file("Manager") # print to excel file reports
        elif option == "9":
            flag_admin = False # sign out
        elif option == "10":
            exit(0)
        else:
            print("You enter worng number\n please try again")


def validate_teacher_exist(teacher_name): #check if teacher exit
    for teacher in teachers_list: # serach the tacher in list of append in manager
        if teacher.username == teacher_name:
            return teacher
    return None


def teacher_options(teacher, flag_teacher):
    while flag_teacher:
        print('1. Add Subject to Student\n')
        print('2. Update grade for Student\n')
        print('3. Print Students grades\n')
        print('4. Print Student grades\n')
        print('5. Print Subject grade\n')
        print('6. Print average grade per subject\n')
        print('7. Output Report\n')
        print('8. Sign Out\n')
        print('9. Quit')
        opt = input()
        if opt == "1":
            student_username = input("Insert student username")
            if student_exist(student_username):
                student_subject = input("Insert subject name")
                student_grade = input("Insert subject grade")
                if not student_grade.isdigit():
                    print("grade must be a number - not a string")
                    continue

                if int(student_grade) >= 0 and int(student_grade) <= 100:
                    subject = Subject(student_subject, int(student_grade))  # send to subject constractor
                    teacher.add_subject_for_student(student_username, subject)  # add the subject for student
                    print("The grade was updated")
                else:
                    print("The number is not valid - must be between 0 -100")
            else:
                print("Not found the student")

        elif opt == "2":
            student_username = input("Insert student username")
            if student_exist(student_username):
                subject_name = input("Insert subject name")
                grade = input("Insert grade")
                if not grade.isdigit():
                    print("grade must be a number - not a string")
                    continue
                if int(grade) >= 0 and int(grade) <= 100:
                    teacher.update_grade_for_student(student_username, subject_name, int(grade)) # update the grade of student
                    print("The grade was updated")
                else:
                    print("The number is not valid - must be between 0 -100")
            else:
                print("Not found the student")
        elif opt == "3":
            teacher.print_students_grade()
        elif opt == "4":
            student_username = input("Insert student username")
            if student_exist(student_username):
                teacher.print_student_grade(student_username)
            else:
                print("No have name student like this")
        elif opt == "5":
            subject = input("Insert subject name")
            teacher.print_subject_grades(subject)
        elif opt == "6":
            subject = input("Insert subject name")
            teacher.print_students_average_subject_grade(subject)
        elif opt == "7":
            export_xlsx_file("Teacher", teacher_obj=teacher)
        elif opt == "8":
            flag_teacher = False
        elif opt == "9":
            exit(0)
        else:
            print("Wrong Number...")

def student_exist(student_username):
    for student in students_list:  # check if the name of student exist
        if student.username == student_username:  # if found the name of student in list
            return True
    return False


def student_options(student, flag_student):
    while flag_student:
        print("1. Watch Grades\n")
        print("2. Output Report\n")
        print("3. Sign Out\n")
        print("4. Exit\n")
        opt = input()
        if opt == "1":
            student.watch_grades()
        elif opt == "2":
            export_xlsx_file("Student", student_obj=student)
        elif opt == "3":
            flag_student = False
        elif opt == "4":
            exit(0)


def register_teacher():
    username = input("What is your username? ")
    password = input("What is your password? ")
    teacher = Teacher(username, password) # constractor


def remove_teacher(teacher_name): # remove teacher from list
    for teacher in teachers_list:
        for k in teacher.keys():
            if teacher.username == teacher_name:
                teachers_list.remove(teacher_name)
                return True
    print("Cant delete the teacher, teacher not found in list")
    return False


def generate_free_time():
    possible_times = 3
    min_time = 8 # strat work at 8:00
    max_time = 17 # finish to work at 17:00
    rng = 1
    for teacher in teachers_list:
        ranges_list = []
        for i in range(possible_times):
            time = random.randint(min_time, max_time)
            until = time + rng
            range_str = str(time) + '-' + str(until)
            ranges_list.append(range_str)
        teacher.free_time = ranges_list


def print_teachers_free_time():
    for teacher in teachers_list:
        print(teacher.username, ' free time: ', teacher.free_time)


def import_csv_file():
    row = []
    with open('input.csv', 'rt') as csvfile:
        file = csv.reader(csvfile, delimiter=',', quotechar='|')
        for r in file:
            row = r
        return row[0],row[1],row[2],row[3]


def export_xlsx_file(role, teacher_obj=None, student_obj=None):
    try:
        workbook = xlsxwriter.Workbook('output.xlsx')
        worksheet = workbook.add_worksheet()
    except ValueError:
        print(ValueError)
        return

    row = 0 #init the rows in file
    col = 0 # init the cols in file

    if role == 'Manager':

        worksheet.write(row, col, 'Teacher')
        row += 1

        for teacher in teachers_list:
            worksheet.write(row, col, teacher.username)
            row += 1

        row += 1
        worksheet.write(row, col, 'Student')
        row += 1

        for student in students_list:
            worksheet.write(row, col, student.username)
            row += 1

        row += 1
        avg_students = 0
        for student in students_list:
            worksheet.write(row, col, student.username)
            for subject in student.subjects:
                worksheet.write(row, col+1, subject.name) # write the name of student
                worksheet.write(row, col+2, subject.grade) # write the grade of student
                row += 1
            worksheet.write(row, col + 1, 'Average:')
            avg_this_student = student.print_student_average_grades()
            avg_students += avg_this_student
            worksheet.write(row, col + 2, avg_this_student) # write the average
            row += 2
        row += 1

        worksheet.write(row, col, 'Students Average:')
        # if teacher_obj is None:
        #     return
        if len(students_list) != 0:
            avg_students /= len(students_list)
        worksheet.write(row, col+1, avg_students) # wirte the average of all students
        row += 1

        worksheet.write(row, col, 'Median:')
        worksheet.write(row, col+1, manager.print_students_median()) # write the median of all students
        row += 1

        worksheet.write(row, col, "Excellent Students:")
        row += 1
        if len(students_list) > 0:
            i = 0
            max_execllent_student=1 # write the excellent of student - can be more one excellent students
            for v in manager.get_excellent_students():
                if i<max_execllent_student:
                    worksheet.write(row, col, v['name']) # the name of student
                    worksheet.write(row, col+1, v['avg']) # the average of student
                    row += 1
                i+=1

            row += 1
            max_execllent_tecaher = 1
            i=0
            for ex in manager.get_excellent_students_by_teacher(): # write the best teacher with the max grade of student of he tech
                if i< max_execllent_tecaher:
                    worksheet.write(row, col, ex['name'])
                    worksheet.write(row, col+1, ex['teacher'])
                    worksheet.write(row, col+2, ex['avg'])
                    row += 1
                i+=1

    elif role == 'Teacher':
        worksheet.write(row, col, 'Student')
        row += 1
        for student in teacher_obj.students:
            worksheet.write(row, col, student.username)
            row += 1
            for subject in student.subjects:
                worksheet.write(row, col, subject.name) # write the name of subject
                worksheet.write(row, col+1, subject.grade) # witre the grade of subject
                row += 1
            row += 1
            worksheet.write(row, col, "Student Average:")
            worksheet.write(row, col+1, teacher_obj.print_student_average(student))
            row += 1

        worksheet.write(row, col, "Average:")
        worksheet.write(row, col+1, teacher_obj.print_students_average()) # the average of all students

    elif role == 'Student':
        worksheet.write(row, col, "Student Grades:")
        row += 1
        for subject in student_obj.subjects:
            worksheet.write(row, col, subject.name)
            worksheet.write(row, col+1, subject.grade)
            row+=1
        row+=1
        worksheet.write(row, col, "Student Average:")
        worksheet.write(row, col+1, student_obj.print_student_average_grades())
        row += 1

    try:
        workbook.close()
        print("Done ! final report was created")
    except IOError:
        print ("Could not Create a file! Please close Excel!")


if __name__ == '__main__':
    manager = Manager('Yoad', '1234') # the username and password of manager
    managers_list.append(manager)
    cconfig_csv = import_csv_file() # inport file
    number_of_students_per_school = int(cconfig_csv[0]) #init
    number_of_students_per_teacher = int(cconfig_csv[1]) #init
    number_of_teachers = int(cconfig_csv[2]) #init
    number_of_managers = int(cconfig_csv[3]) #init
    main_options() #main option

