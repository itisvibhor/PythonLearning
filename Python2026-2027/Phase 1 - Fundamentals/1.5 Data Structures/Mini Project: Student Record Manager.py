# Mini Project : Student Record Manager
students = []
def add_student():
    global students
    student_count = int(input("Enter No. Of Student's Data You Want To Enter : "))
    for i in range(student_count):
        student_marks_list = []
        student_name = input(f"Enter Name of Student {i+1} : ")
        student_age = int(input(f"Enter Age of Student {i+1} : "))
        student_subjects = int(input("Enter Subject's Count : "))
        for j in range(student_subjects):
            student_marks =int(input(f"Enter Marks of Subject {j+1} : "))
            student_marks_list.append(student_marks)

        students_dict = {   
        "name" : student_name,
        "age" : student_age,
        "marks" : student_marks_list
    }
        students.append(students_dict)

    return students

def search_student_by_name():
    flag = 0
    find_name = input("Enter Name To Search : ")
    for i in range(0,len(students)):
        if(students[i]["name"] == find_name):
            flag = flag + 1
            for keys,values in students[i].items():
                print(keys , values)
            break
               
    if flag < 1:
        print("Student Not Found")

while True:
    print(" ----------- Menu ----------- ")
    print("Option 1 - Add new Student ")
    print("Option 2 - Show All Student Details ")
    print("Option 3 - Search Student by Name " )
    print("Option 4 - Exit " )
    option = int(input("Enter Your Option No. : "))
    if option == 1:
        result = add_student()
    elif option == 2:
        if students == []:
            print("Kindly add some data first and Try Again", end = '\n')
        else:
            for i in students:
                for keys,values in i.items():
                    print(f" {keys} : {values}")
    elif option == 3:
        if students == []:
                    print("Kindly add some data first and Try Again", end = '\n')
        else:
             search_student_by_name()
    elif option == 4:
        break
    else:
        print("Invalid Option! Try Again...")

