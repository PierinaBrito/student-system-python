from statistics import mean

students = {}

def accept_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = float(input("Enter student's grade: "))
    students[student_id] = {"Name": name, "Grade": grade}
    print("Student added successfully!")

def display_students():
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['Name']}, Grade: {info['Grade']}")

def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        print(f"Found: ID: {student_id}, Name: {students[student_id]['Name']}, Age: {students[student_id]['Age']}")
    else:
        print("Student not found.")

def calculate_average(student):
    sum = 0
    for number in student:
        sum += number
    average = sum / len (student)
    return average

def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Enter Student's Information")
        print("2. Display Students")
        print("3. Search Student")
        print("4: Calculate class average")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            accept_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            calculate_average()
        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please choose again.")


if __name__ == "__main__":
    main_menu()

#search by name, add more searchability (put another if statement)
#file handling and export it to the file
#bonus: grade categorizations
#dictionary if we wanted to do it by different subjects
