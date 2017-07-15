import random

profession_teachers = []
profession_students = []
profession_grades = []
profession = ["Jewry","History","English","Math","Computers","Science"]


def insertGrades(username):
    print("insertGrades")
    student = input("What your student name of you want to update his grade? \n")
    profession = input("Please enter thr profession of student\n")
    for x in range(len(profession_students)):
        if profession_students[x][0] == student and profession_students[x][2] == username and profession_students[x][1] == profession:
            grade = input("please enter the grade of student\n")
            profession_grades.append((student, profession,username,grade))


    print(profession_grades)

def seeCalcGrades():
    print("seeCalcGrades")

def registerTeacher(arrayTeacher):
    print("registerTeacher")
    username = input("What is your username? ")
    password = input("What is your password? ")
    arrayTeacher[username] = password
    #for i in range(len(profession)):
    #     profession_teachers.append((username,profession[i]))
    # print(profession_teachers)

def registerStudent(arrayStudent,arrayTeacher):
    print("registerStudent")
    username = input("What is your username? ")
    password = input("What is your password? ")
    arrayStudent[username] = password
    i = 0
    while (i < len(profession)):
        print("Answer yes or leave it")
        print(username, "is studing ", profession[i], "?")
        answer = input()
        if answer == "yes":
            teacher = random.randint(0, len(arrayTeacher) - 1) # choose random teacher from all teachers
            profession_students.append((username, profession[i],list(arrayTeacher)[teacher],0)) # take the key from dist of tachers
       # if profession_teachers
        i += 1
    print(profession_students)

def signTeacher(arrayTeacher):
    print("signTeacher")
    username = input("What is your username? ")
    password = input("What is your password? ")
    if username in arrayTeacher.keys():
        expected_password = arrayTeacher[username]
        if expected_password == password:
            print ("Welcome ,", username)
            while(True):
                print("please choose one of option")
                print("1. Update grades")
                print("2. See grades")
                print("3. Back to main")
                option = input()
                if option == "3":
                    break
                elif option == "2":
                    seeCalcGrades()
                elif option == "1":
                    insertGrades(username)
                else:
                    print("Worng option, please try again")
        else:
            print("Didn't you forget your password,", username)
    else:
        print("Unknown user")

def signStudent():
    print("signStudent")

def main():
    arrayTeacher = {}
    arrayStudent = {}
    while(True):
        print("please choose one of option:\n")
        print("1. Register Teacher\n")
        print("2. Register Student\n")
        print("3. Sign in as Teacher\n")
        print("4. Sign in as Student\n")
        print("5. Update Name of Teacher\n") #TODO : implemation this function
        print("6. Update Name of Student\n") #TODO : implemation this function
        print("7. Quit")
        option = input()
        if option == "1":
            registerTeacher(arrayTeacher)
        elif option == "2":
            registerStudent(arrayStudent,arrayTeacher)
        elif option == "3":
            signTeacher(arrayTeacher)
        elif option == "4":
            signStudent(arrayStudent)
        elif option == "7":
            exit(0)
        else:
            print("You enter worng number\n please try again")
        print(arrayTeacher)

if __name__ == '__main__':
    main()