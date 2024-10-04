#  Student Grades Management System
# • Create a program that allows users to input student names and grades. The program should be
# able to calculate the class average, highest and lowest grades, and display all students' grades.
# • Bonus: Add features such as grade categorization (e.g., A, B, C) and handling missing data.
# • Focus Areas: Lists, dictionaries, loops, conditional logic, and file handling (optional).


# THIS FUNCTION WILL ADD STUDENT INFORMATION.
# THE INFORMATION ADDED WILL BE STORE IN THE STUDENT LIST, AND CAN BE DISPLAY OR SEARCH LATER.
# START BY ASSUMING THE STUDENT IS NOT IN THE SYSTEM.
# THE P VARIABLE WILL CHECK IF THE STUDENT-ID IS ALREADY EXIST, TO AVOID REPEAT VALUES.
def add_student():
    found = False  # Start by assuming the student is not found
    print("\n--------------------")
    student_ID = input("Enter Student_ID: ")

    # Check if the student ID already exists
    for p in student:
        if student_ID == p["Student_ID"]:
            found = True  # Student ID found, so no need to add again
            break

    # If not found, add a new student
    if not found:
        name = input("Enter Name: ")
        sub = input("Enter Subject: ")
        grade = input("Enter Grade: ")
        rec = {"Student_ID": student_ID, "Name": name, "Subject": sub, "Grade": grade}
        student.append(rec)
        print("--------------------")
        print("Student record added successfully!")
        print("--------------------")
    else:
        print("\n--------------------")
        print("Student-ID is already in the system.")
        print("--------------------\n")


# THIS FUNCTION WILL DISPLAY STUDENT INFORMATION.
# THE FOR LOOP IS IMPLEMENTED IN THIS FUNCTION IN ORDER TO DISPLAY STUDENT INFORMATION.
# THE FOR LOOP WILL BE EXECUTED 10 TIMES.
# THE VARIABLE i IS DECLARED TO STORE STUDENT LIST THAT CONTAIN ALL STUDENT DATA.
# NULL PRINT FUNCTION CONTAIN EMPTY STRING AND IS IMPLEMENT HERE TO SEPARATE ONE OUTPUT TO OTHER OUTPUT.

def display_students():
    found = False
    print("\n--------------------------------")
    for i in student:
        found = True
        print("Student_ID: ",i["Student_ID"])
        print("Name: ", i["Name"])
        print("Subject: ", i["Subject"])
        print("Grade: ", int(i["Grade"]))
        print("--------------------\n")

    if not found:
        print("\n-----------------------------------------")
        print("No Student data Found. Please Add Student")
        print("-----------------------------------------\n")


# THIS DEFINE THE SEARCH FUNCTION THAT WILL BE SEARCH FOR THE INFORMATION OF A SPECIFIC STUDENT.
# usi (USER STUDENT ID) IS A FUNCTION THAT WILL HELP TO MATCH WHEN THE USER SEARCH WITH THE STUDENT ID THAT IS STORE IN THE STUDENT LIST.
# IF THERE IS AN INVALID STUDENT ID, THE USER WILL BE GET A MESSAGE.
def search_student():
    found = False
    print("\n--------------------------------")
    usi = input("Enter a Specific Student Id:")
    for j in student:
        if usi == j["Student_ID"]:
            found = True
            print("Student_ID: ", j["Student_ID"])
            print("Name: ", j["Name"])
            print("Subject: ", j["Subject"])
            print("Grade: ", j["Grade"])
            # Get the grade value for the calculation and determine what is the corresponding letter grade
            grade = int(j["Grade"])
            if grade >= 90:
                print('Letter Grade: A')
            elif grade >= 80:
                print('Letter Grade: B')
            elif grade >= 70:
                print('Letter Grade: C')
            elif grade >= 60:
                print('Letter Grade: D')
            else:
                print('Letter Grade: F')
            print("--------------------\n")
            break
    if not found:
        print("\n--------------------")
        print("Student Not Found")
        print("--------------------\n")

def calculate_grade_average():
    sum_of_grades = 0
    count = 0

    for record in student:
        grade = int(record["Grade"])
        sum_of_grades += grade
        count += 1
    if count > 0:
        average_grade = sum_of_grades / count
        return average_grade
    else:
        return None

def calculate_max_grade():
    max_grade = None

    for record in student:
        grade = int(record["Grade"])
        if max_grade is None or grade > max_grade:
            max_grade = grade
    return max_grade

#
# THERE ARE 4 OPTIONS THAT THE USER CAN CHOOSE.
# THE PRINT FUNCTION DISPLAY THE DIFFERENT OPTIONS FOR THE USER.
# IF THERE IS AN INVALID VALUE, THE USER WILL BE GET A MESSAGE.

student = []
print("\n-----------------------------------------------")
print("Welcome to the Student Grades Management System")
print("------------------------------------------------\n")
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Display Average Grade")
    print("5. Display Highest Grade")
    print("6. Exit")
    op = int(input("Enter Your Choice: "))
    print("--------------------\n")

    if op == 1:
        add_student()
    elif op == 2:
        display_students()
    elif op == 3:
        search_student()
    elif op == 4:
        average_grade = calculate_grade_average()
        if average_grade is not None:
            print("Average Grade: ", average_grade)
        else:
            print("No Students Found.")
    elif op == 5:
        max_grade = calculate_max_grade()
        if max_grade is not None:
            print("Max Grade: ", max_grade)
        else:
            print("No Students Found.")
    elif op == 6:
        print("Thank you, have a nice day! \n")
        break
    else:
        print("\n--------------------")
        print("Invalid input")
        print("--------------------\n")