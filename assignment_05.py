#---------------------------------------------------------------------------------- #
#Title: Assignment05
#Desc: Advanced Collections and Error Handling
#Change Log: (Who, When, What)
#Disha, 8/28/2024,Created Script
#---------------------------------------------------------------------------------- #
import csv

MENU: str='''\n--- Course Registration Program ---
Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------'''
FILE_NAME: str = "Enrollments.csv"

# Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: dict = []
students: list = []
parts: list = []

# When the program starts, read the file data into a dictionary rows (tables)
try:
    file = open(FILE_NAME, 'r')
     # Transform the data from the file
    for row in file.readlines():
        parts = row.strip().split(",")
        student_first_name = parts["first_name"]
        student_last_name = parts["last_name"]
        course_name = parts["course_name"]
        student_data = {'First_Name': student_first_name, 'Last_Name': student_last_name, 'Course_name': course_name}
        students.append(student_data)
        file.close()
    # Extract the data from the file, with added exception handling
except FileNotFoundError as errortext:
        print("Text file must exist before running this script!\n")
except Exception as errortext:
        print("There was a non-specific error!\n")
        print("Built-In Python error info: ")
        print(errortext, errortext.__doc__, type(errortext), sep='\n')
finally:
        if file.closed == False:
            file.close()
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == '1':
        try:
            # Input the data:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student First Name must be alphabetic")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student Last Name must be alphabetic")
            course_name = input("Please enter the name of the course: ")
            students = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            student_data.append(students)
            csv_data += f"{student_first_name},{student_last_name},{course_name}\n"
        except ValueError as errortext:
            print(errortext)
            print('---Technical Information---')
            print(errortext.__doc__, type(errortext), sep='\n')

    elif menu_choice == '2':
        for students in student_data:
            student_first_name = students['first_name']
            student_last_name = students['last_name']
            course_name = students['course_name']
        if csv_data:
            print("\nThe Current Data is:")
            print(csv_data)
        else:
            print(" ")
        continue

    elif menu_choice == '3':
        try:
            file = open(FILE_NAME, 'w')
            for students in student_data:
                student_first_name = students['first_name']
                student_last_name = students['last_name']
                course_name = students['course_name']
                file.write(f"{student_first_name},{student_last_name},{course_name}\n")
            file.close()
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}')
            continue
        except TypeError as errortext:
            print(errortext)
            print('---Technical Information---')
            print(errortext.__doc__, type(errortext), sep='\n')
        except Exception as errortext:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(errortext, errortext.__doc__, type(errortext), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    elif menu_choice == '4':
        print("Program Ended")
        break

    else:
        print("You made invalid choice. Please try again. ")

