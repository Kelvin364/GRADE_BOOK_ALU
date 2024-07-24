from gradebook import GradeBook, Student, Course
from tabulate import tabulate

def teacher_menu(gradebook):
    while True:
        print("\nTeacher Menu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by GPA Range")
        print("7. Generate Transcript")
        print("8. Exit to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            content = input("Enter the URL for the lesson content: ")
            evaluation = []
            for i in range(5):
                question = input(f"Enter question {i + 1}: ")
                options = [input(f"Option {j + 1}: ") for j in range(4)]
                correct_option = int(input("Enter the correct option (1-4): ")) - 1
                evaluation.append({'question': question, 'options': options, 'correct_option': correct_option})
            course = Course(name, trimester, credits, content, evaluation)
            gradebook.add_course(course)
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            gradebook.register_student_for_course(student_email, course_name)
        elif choice == '4':
            student_email = input("Enter student email: ")
            gpa = gradebook.calculate_GPA(student_email)
            print(f"GPA of {student_email}: {gpa}")
        elif choice == '5':
            ranking = gradebook.calculate_ranking()
            print("Student Ranking by GPA:")
            table = [[i + 1, student.names, student.GPA] for i, student in enumerate(ranking)]
            headers = ["Rank", "Student Name", "GPA"]
            print(tabulate(table, headers, tablefmt="grid"))
        elif choice == '6':
            min_gpa = float(input("Enter minimum GPA: "))
            max_gpa = float(input("Enter maximum GPA: "))
            students = gradebook.search_by_GPA_range(min_gpa, max_gpa)
            print(f"Students with GPA between {min_gpa} and {max_gpa}:")
            table = [[student.names, student.email, student.GPA] for student in students]
            headers = ["Student Name", "Email", "GPA"]
            print(tabulate(table, headers, tablefmt="grid"))
        elif choice == '7':
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(f"Transcript for {student_email}:")
                table = [[course['name'], course['trimester'], course['credits'], course['grade']] for course in transcript['courses']]
                headers = ["Course Name", "Trimester", "Credits", "Grade"]
                print(tabulate(table, headers, tablefmt="grid"))
                print(f"GPA: {transcript['GPA']}")
            else:
                print("Student not found.")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu(gradebook):
    email = input("Enter your email: ")
    name = input("Enter your name: ")
    student = next((s for s in gradebook.student_list if s.email == email and s.names == name), None)

    if not student:
        print("Student not found.")
        return

    while True:
        print("\nStudent Menu:")
        print("1. View Courses")
        print("2. Learn Course Content")
        print("3. Take Test")
        print("4. View Transcript")
        print("5. Exit to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            if student.courses_registered:
                print("Courses you are enrolled in:")
                table = [[course.name, course.trimester, course.credits, course.grade] for course in student.courses_registered]
                headers = ["Course Name", "Trimester", "Credits", "Grade"]
                print(tabulate(table, headers, tablefmt="grid"))
            else:
                print("You are not enrolled in any courses.")
        elif choice == '2':
            if student.courses_registered:
                for course in student.courses_registered:
                    print(f"Course: {course.name}")
                    print(f"Content URL: {course.content}")
            else:
                print("You are not enrolled in any courses.")
        elif choice == '3':
            if student.courses_registered:
                course_name = input("Enter the course name to take the test: ")
                student.take_test(course_name)
            else:
                print("You are not enrolled in any courses.")
        elif choice == '4':
            transcript = gradebook.generate_transcript(email)
            if transcript:
                print(f"Transcript for {email}:")
                table = [[course['name'], course['trimester'], course['credits'], course['grade']] for course in transcript['courses']]
                headers = ["Course Name", "Trimester", "Credits", "Grade"]
                print(tabulate(table, headers, tablefmt="grid"))
                print(f"GPA: {transcript['GPA']}")
            else:
                print("Student not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    gradebook = GradeBook()

    while True:
        print("\n------Welcome to the ALU School system------")
        print("\nMain Menu:")
        print("1. Teacher")
        print("2. Student")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            email = input("Enter your email: ")
            if email.endswith('@alueducation.com'):
                teacher_menu(gradebook)
            else:
                print("Invalid email. Access denied.")
        elif choice == '2':
            student_menu(gradebook)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
