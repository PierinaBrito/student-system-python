#  Student Grades Management System
# • Create a program that allows users to input student names and grades. The program should be
# able to calculate the class average, highest and lowest grades, and display all students' grades.
# • Bonus: Add features such as grade categorization (e.g., A, B, C) and handling missing data.
# • Focus Areas: Lists, dictionaries, loops, conditional logic, and file handling (optional).


import os

# THIS FUNCTION WILL ADD STUDENT INFORMATION.
# THE INFORMATION ADDED WILL BE STORE IN THE STUDENT LIST, AND CAN BE DISPLAY OR SEARCH LATER.
# START BY ASSUMING THE STUDENT IS NOT IN THE SYSTEM.
# THE P VARIABLE WILL CHECK IF THE STUDENT-ID IS ALREADY EXIST, TO AVOID REPEAT VALUES.
def add_std():
    found = False  # START BY ASSUMING THE STUDENT IS NOT FOUND.
    print()
    print("--------------------")
    student_Id = input("Enter Student_Id: ")

    # CHECK IF THE STUDENT ID IS IN THE SYSTEM
    for p in student:
        if student_Id == p["Student_Id"]:
            found = True  # IF ID STUDENT IS NOT FOUND, WILL ASK YOU TO ADD IT.
            break
        
    if not found:
        name = input("Enter Name: ")
        sub = input("Enter Subject: ")
        grade = input("Enter Grade: ")
        rec = {"Student_Id": student_Id, "Name": name, "Subject": sub, "Grade": grade}
        student.append(rec)
        print()
        print("--------------------")
        print("Student record added successfully!")
        print("--------------------")
        print()
    else:
        print()
        print("--------------------")
        print("Student-ID is already in the system.")
        print("--------------------")
        print()


# THIS FUNCTION WILL DISPLAY STUDENT INFORMATION.
# THE FOR LOOP IS IMPLEMENTED IN THIS FUNCTION IN ORDER TO DISPLAY STUDENT INFORMATION.
# THE FOR LOOP WILL BE EXECUTED 10 TIMES.
# THE VARIABLE i IS DECLARED TO STORE STUDENT LIST THAT CONTAIN ALL STUDENT DATA.
# NULL PRINT FUNCTION CONTAIN EMPTY STRING AND IS IMPLEMENT HERE TO SEPARATE ONE OUTPUT TO OTHER OUTPUT.

def dis_std():
    found = False
    print()
    print("--------------------")
    for i in student:
        found=True
        print("Student_Id: ",i["Student_Id"])
        print("Name: ", i["Name"])
        print("Subject: ", i["Subject"])
        print("Grade: ", i["Grade"])
        print("--------------------")
        print()

    if not found:
        print()
        print("-----------------------------------------")
        print("No Student data Found. Please Add Student")
        print("-----------------------------------------")
        print()

    return found


#THIS FUNCTION WILL DISPLAY THE EQUIVALENT OF THE GRADES IN LETTERS.

def get_letter_grade(grade):
    if grade >= 0 and grade <= 30:
        return "F"
    elif grade >= 31 and grade <= 55:
        return "D"
    elif grade >= 56 and grade <= 73:
        return "C"
    elif grade >= 74 and grade <= 89:
        return "B"
    elif grade >= 90 and grade <= 94:
        return "A"
    elif grade >= 95 and grade <= 100:
        return "A+"
    return "Invalid"

# THIS FUNCTION WILL DISPLAY STUDENT'S GRADES IN LETTERS.
# HERE YOU WILL GET ALSO THE MAXIMUM STUDENT GRADES.
# THE DISPLAY FUNCTION IS CALLED HERE TO SHOW THE STORE STUDENTS AND WITH THE GRADE FUNCTION
# WILL COMPARE THE NUMBERS IN LETTERS.
def grades():
    stu_grades = []

    # THE dis_std FUNCTION IS CALLED HERE TO DISPLAY THE STUDENTS IN THE SYSTEM.
    if not dis_std():
        return  # IF THE STUDENT IS NOT IN THE SYSTEM OR IS NOT FOUND, WILL SHOW A MESSAGE.

    # A LOOP TO INPUT GRADES FOR STUDENTS.
    for i in range(len(student)):
        try:
            grade = int(input(f"Enter the grade for student {student[i]['Name']} (ID: {student[i]['Student_Id']}): "))
            stu_grades.append(grade)
        except ValueError:
            print("Please enter a valid integer.")

    # HERE DISPLAY THE GRADES WITH THEIR CORRESPONDING CATEGORIES
    for u in range(len(stu_grades)):
        letter_grade = get_letter_grade(stu_grades[u])
        print(f"Student {student[u]['Name']} (ID: {student[u]['Student_Id']}) is graded {letter_grade}")

    # THIS CONVERT THE MAXIMUM STUDENTS GRADES IN LETTER FORM.
    if stu_grades:
        max_grade = max(stu_grades)
        max_student_index = stu_grades.index(max_grade)
        max_letter_grade = get_letter_grade(max_grade)
        print(f"\nThe student with the highest grade is {student[max_student_index]['Name']} (ID: {student[max_student_index]['Student_Id']}) with a grade of {max_letter_grade}.")

    print(f"\nTotal of Students' Grades: {stu_grades}\n")


# THIS DEFINE THE SEARCH FUNCTION THAT WILL BE SEARCH FOR THE INFORMATION OF A SPECIFIC STUDENT.
# usi (USER STUDENT ID) IS A FUNCTION THAT WILL HELP TO MATCH WHEN THE USER SEARCH WITH THE STUDENT ID THAT IS STORE IN THE STUDENT LIST.
# IF THERE IS AN INVALID STUDENT ID, THE USER WILL BE GET A MESSAGE.

def search():
    found=False
    print()
    print("--------------------------------")
    usi=input("Enter a Specific Student Id or Name: ")
    for j in student:
        if usi==j["Student_Id"] or usi ==j ["Name"]:
            found=True
            print("Student_Id: ", j["Student_Id"])
            print("Name: ", j["Name"])
            print("Subject: ", j["Subject"])
            print("Grade: ", j["Grade"])
            print("--------------------")
            print()
            break
    if not found:
        print()
        print("--------------------")
        print("Student Not Found")
        print("--------------------")
        print()


# THIS DISPLAY FILE TEXT WITH STUDENT HISTORY RECORD PER YEAR
# r = READ THIS FUNCTION WILL PRINT THE INFORMATION THAT IS IN THE TEXT FILE.
# a = APPEND FUNCTION IS AVAILABLE TO RUN IF WE WANT TO ADD A NEW STUDENT IN THE TEXT FILE.
# w = Overwrite - THIS FUNCTION WILL DELETE THE CONTENT IN THE FILE AND WILL OVERWRITE NEW INFORMATION
# x = CREATE A FILE FOR WRITING OR CREATES THE FILE IF IT DOES NOT EXIST.
# DELETED FUNCTION IS AVAILABLE IF WE WANT TO DELETE A FILE.
# ERROR MESSAGE WILL RETURN WHEN A TEXT FILE IS NOT IN THE SYSTEM.

def record():

# Append - ADD DATA TO THE FILE
#    f = open("record.txt", "a")
#    f.write("Andrew 87\n")

# Write - OVERWRITE
#    f = open("record.txt", "w")
#    f.write("Updated the Record")

# Create A NEW FILE
#    if not os.path.exists("record_2024.text"):
#        f = open("example.text", "x")

# THIS CODE WILL DELETE A FILE
#    if not os.path.exists("example.text"):
#       os.remove("example.text")
#    else:
#        print("The file you want to delete does not exist")
#        f.close()


# Read - PRINT THE INFORMATION THAT IS IN THE FILE
    f = open("record.txt")
    print(f.read())
    print()
    print("--------------------")
    f.close()

    print()
    print("-----------------------------------------------")
    print("------------STUDENTS 2023 HISTORY--------------")
    print("-----------------------------------------------")
    print()
    t = open("school.csv")
    print(t.read())
    print()
    print("--------------------")
    t.close()

#    try:
#        f = open("record.txt")
#        print(f.read())
#    except:
#        print("The file you want to read doesn't exist")
#    finally:
#       f.close()


# THERE ARE 4 OPTIONS THAT THE USER CAN CHOOSE.
# THE PRINT FUNCTION DISPLAY THE DIFFERENT OPTIONS FOR THE USER.
# IF THERE IS AN INVALID VALUE, THE USER WILL BE GET A MESSAGE.

student=[]
print()
print("-----------------------------------------------")
print("Welcome to the Student Grades Management System")
print("------------------------------------------------")
print()
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Average Student Grades")
    print("5. Students History Record")
    print("0. Exit")
    op=int(input("Enter Your Choice: "))
    print("------------------------------")
    print()

    if op==1:
        add_std()
    elif op==2:
        dis_std()
    elif op==3:
        search()
    elif op==4:
        grades()
    elif op==5:
        record()
    elif op==0:
        print("Thank you, have a nice day! \n")
        break

    #elif op==0:
     #   break
    else:
        print()
        print("--------------------")
        print("Invalid input")
        print("--------------------")
        print()