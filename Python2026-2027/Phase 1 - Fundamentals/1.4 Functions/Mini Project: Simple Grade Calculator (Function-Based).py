# Simple Grade Calculator
def calculate_avg(marks_list):
    total = 0
    for i in marks_list:
        total = total + i
    return total/len(marks_list)

def calculate_grade(avg_marks):
    if avg_marks >=90:
        return "A"
    elif  75 <= avg_marks <= 89:
        return "B"
    elif  65 <= avg_marks <= 74:
            return "C"
    else:
         return "F" 

marks_list = []
student_name = input("Enter Student's Name : ")
while True:
    subject_count = int(input("Enter No. Of Subject Marks You want to enter : "))
    if subject_count <= 0:
         print("Subject Cannot be 0 or negative. Please Try Again")
    else:
         break
    
for i in range(subject_count):
    marks = float(input(f"Enter Marks for Subject {i+1} : "))
    marks_list.append(marks)

avg_marks = calculate_avg(marks_list)
grade = calculate_grade(avg_marks)
print(f"REPORT CARD OF {student_name}")
print("Avg Marks Are : " , round(avg_marks,2))
print(f"Your Grade Is : {grade}")