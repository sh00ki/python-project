from student import Student
from teacher import Teacher
from manager import Manager
from subject import Subject
import random
import csv
import xlsxwriter

managers_list = []
teachers_list = []
students_list = []
flag_admin = False


def main_options():
    while (True):
        print("Please choose one of options:\n")
        print('1. Login as Manager\n')
        print('2. Login as Teacher\n')
        print('3. Login as Student\n')
        print('4. Quit\n')

        opt = input()
        if opt == '1':
            username = input("What is your username? ")
            password = input("What is your password? ")
            if manager.username == username and manager.password == password:
                print('Welcome ', manager.username)
                flag_admin = True
                manager_options(flag_admin)

        elif opt == '2':
            username = input("What is your username? ")
            password = input("What is your password? ")
            for teacher in manager.teachers:
                if teacher.username == username and teacher.password == password:
                    print('Welcome ', teacher.username)
                    flag_teacher = True
                    teacher_options(teacher, flag_teacher)
        elif opt == '3':
            username = input("What is your username? ")
            password = input("What is your password? ")
            for student in students_list:
                if student.username == username and student.password == password:
                    print('Welcome ', student.username)
                    flag_student = True
                    student_options(student, flag_student)
        elif opt == '4':
            exit(0)
        else:
            continue


def manager_options(flag_admin):

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
        if option == "1":
            teacher_username = input("Insert teacher username")
            teacher_password = input("Insert teacher password")
            if len(teachers_list) <= number_of_teachers:
                teacher = Teacher(teacher_username, teacher_password)
                manager.add_teacher(teacher)
                teachers_list.append(teacher)
            else :
                print("Can't register more teachers to school!")
        elif option == "2":
            teacher_username = input("Insert teacher username")
            teacher_new_username = input("Insert teacher new username")
            manager.update_teacher(teacher_username, teacher_new_username)
        elif option == "3":
            teacher_username = input("Insert teacher username")
            manager.remove_teacher(teacher_username)
            for teacher in teachers_list:
                if teacher.name == teacher_username:
                    teachers_list.remove(teacher)
        elif option == "4":
            student_username = input("Insert student username")
            student_password = input("Insert student password")
            for r in students_list:
                for d in r:
                    if d['username'] == student_username:
                        print('The student ', student.username, ' was registred.')
                        return
            if len(students_list) <= number_of_students_per_school:
                print('The student',student_username, 'has added to list')
                teacher_username = input("Insert teacher username")
                if validate_teacher_exist(teacher_username):
                    if len(teacher.students) < number_of_students_per_teacher:
                        # TODO - check if the teacher exists
                        student = Student(student_username, student_password)
                        manager.add_student_for_teacher(teacher_username, student)
                        students_list.append(student)
                    else:
                        print("The teacher ", teacher_username, "is full ! - cant register more students to this teacher")
                else:
                    print("The student ", student_username, " was deleted because he doesn't have teacher")
            else:
                print("The school is full students, can't register more students")

        elif option == "5":
            student_username = input("Insert student username")
            teacher_username = input("Insert teacher username")
            manager.remove_student_from_teacher(student_username, teacher_username)
            for student in students_list:
                if student.name == student_username:
                    students_list.remove(student)
        elif option == "6":
            generate_free_time()
        elif option == "7":
            print_teachers_free_time()
        elif option == "8":
            export_xlsx_file("Manager")
        elif option == "9":
            flag_admin = False
        elif option == "10":
            exit(0)
        else:
            print("You enter worng number\n please try again")


def validate_teacher_exist(teacher_name):
    for teacher in teachers_list:
        if teacher.username == teacher_name:
            return True
    return False


def teacher_options(teacher,flag_teacher):
    profession = ["Jewry", "History", "English", "Math", "Computers", "Science"]
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
            student_subject = input("Insert subject name") #TODO : need to validate the subject by profession
            student_grade = input("Insert subject grade")
            subject = Subject(student_subject,student_grade)
            teacher.add_subject_for_student(student_username, subject)
        elif opt == "2":
            student_username = input("Insert student username")
            subject_name = input("Insert subject name")
            grade = input("Insert grade")
            teacher.update_grade_for_student(student_username, subject_name, grade)
        elif opt == "3":
            teacher.print_students_grade()
        elif opt == "4":
            student_username = input("Insert student username")
            teacher.print_student_grade(student_username)
        elif opt == "5":
            subject = input("Insert subject name")
            teacher.print_subject_grades(subject)
        elif opt == "6":
            subject = input("Insert subject name")
            teacher.print_students_average_subject_grade(subject)
        elif opt == "7":
            export_xlsx_file("Teacher")
        elif opt == "8":
            flag_teacher = False
        elif opt == "9":
            exit(0)
        else:
            print("Wrong Number...")


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
            export_xlsx_file("Student")
        elif opt == "3":
            flag_student = False
        elif opt == "4":
            exit(0)


def register_teacher():
    username = input("What is your username? ")
    password = input("What is your password? ")
    teacher = Teacher(username, password)


def remove_teacher(teacher_name):
    for teacher in teachers_list:
        for k in teacher.keys():
            if teacher.username == teacher_name:
                teachers_list.remove(teacher_name)


def generate_free_time():
    possible_times = 3
    min_time = 8
    max_time = 17
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


def prepare_data(role):
    data = []
    if role == 'Manager':
        data = prepare_manager_data()
    elif role == 'Teacher':
        data = prepare_teacher_data()
    elif role == 'Student':
        data = prepare_student_data()
    return data


def prepare_manager_data():
    data = []
    for teacher in teachers_list:
        data.append(teacher)
        for student in teacher.students:
            data.append(student)
            for subject in student.subjects:
                data.append(subject)
    return data


def prepare_teacher_data(teacher):
    data = []
    for student in teacher.students:
        data.append(student)
        for subject in student.subjects:
            data.append(subject)
    return data


def prepare_student_data(student):
    data = []
    for subject in student.subjects:
        data.append(subject)
    return data


# def export_csv_file(fields_names, data):
#     with open('output.csv', 'w') as csvfile:
#
#         writer = csv.DictWriter(csvfile, fieldnames=fields_names)
#         writer.writeheader()
#
#         for r in data:
#             writer.writerow(r)


def export_xlsx_file(role):
    workbook = xlsxwriter.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

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
        for student in students_list:
            worksheet.write(row, col, student.username)
            for subject in student.subjects:
                worksheet.write(row, col+1, subject.name)
                worksheet.write(row, col+2, subject.grade)
                row += 1
            worksheet.write(row, col + 1, 'Average:')
            worksheet.write(row, col + 2, student.print_student_average_grades())
        row += 1



    elif role == 'Teacher':
        pass

    elif role == 'Student':
        pass


    workbook.close()


if __name__ == '__main__':
    manager = Manager('Yoad', '1234')
    managers_list.append(manager)
    cconfig_csv = import_csv_file()
    print(cconfig_csv[0],cconfig_csv[1],cconfig_csv[2],cconfig_csv[3])
    number_of_students_per_school = int(cconfig_csv[0])
    number_of_students_per_teacher = int(cconfig_csv[1])
    number_of_teachers = int(cconfig_csv[2])
    number_of_managers = int(cconfig_csv[3])
    main_options()

