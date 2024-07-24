import csv

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        total_credits = sum(course.credits for course in self.courses_registered)
        if total_credits == 0:
            return 0
        total_points = sum((course.grade / 100) * course.credits for course in self.courses_registered)
        self.GPA = total_points
        return self.GPA

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def take_test(self, course_name):
        course = next((c for c in self.courses_registered if c.name == course_name), None)
        if not course:
            print("You are not registered for this course.")
            return

        correct_answers = 0
        for question in course.evaluation:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            answer = input("Enter your choice (1-4): ")
            if question['correct_option'] == int(answer) - 1:
                correct_answers += 1

        grade = (correct_answers / 5) * 100
        course.grade = grade
        self.calculate_GPA()
        print(f"Your grade for {course_name} is: {grade}")

    def to_csv_row(self):
        return [self.email, self.names, ','.join(course.name for course in self.courses_registered), self.GPA]

    @staticmethod
    def from_csv_row(row, courses):
        email, names, courses_registered_str, GPA = row
        student = Student(email, names)
        student.GPA = float(GPA)
        course_names = courses_registered_str.split(',')
        student.courses_registered = [course for course in courses if course.name in course_names]
        return student


class Course:
    def __init__(self, name, trimester, credits, content="", evaluation=None, grade=0):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.content = content
        self.evaluation = evaluation if evaluation else []
        self.grade = grade

    def to_csv_row(self):
        evaluation_str = ';'.join([f"{q['question']}|{','.join(q['options'])}|{q['correct_option']}" for q in self.evaluation])
        return [self.name, self.trimester, self.credits, self.content, evaluation_str, self.grade]

    @staticmethod
    def from_csv_row(row):
        name, trimester, credits, content, evaluation_str, grade = row
        evaluation = []
        for eval_item in evaluation_str.split(';'):
            question, options, correct_option = eval_item.split('|')
            options = options.split(',')
            evaluation.append({'question': question, 'options': options, 'correct_option': int(correct_option)})
        return Course(name, trimester, int(credits), content, evaluation, float(grade))


class GradeBook:
    def __init__(self, students_file='students.csv', courses_file='courses.csv'):
        self.students_file = students_file
        self.courses_file = courses_file
        self.student_list = self.load_students()
        self.course_list = self.load_courses()

    def add_student(self, student):
        self.student_list.append(student)
        self.save_students()

    def add_course(self, course):
        self.course_list.append(course)
        self.save_courses()

    def register_student_for_course(self, student_email, course_name):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course)
            self.save_students()

    def calculate_GPA(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            gpa = student.calculate_GPA()
            self.save_students()
            return gpa
        return None

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_GPA_range(self, min_gpa, max_gpa):
        return [student for student in self.student_list if min_gpa <= student.GPA <= max_gpa]

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            return {
                'email': student.email,
                'names': student.names,
                'GPA': student.GPA,
                'courses': [{'name': course.name, 'trimester': course.trimester, 'credits': course.credits, 'grade': course.grade} for course in student.courses_registered]
            }
        return None

    def load_students(self):
        students = []
        courses = self.load_courses()
        try:
            with open(self.students_file, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                for row in reader:
                    students.append(Student.from_csv_row(row, courses))
        except FileNotFoundError:
            pass
        return students

    def save_students(self):
        with open(self.students_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['email', 'names', 'courses_registered', 'GPA'])
            for student in self.student_list:
                writer.writerow(student.to_csv_row())

    def load_courses(self):
        courses = []
        try:
            with open(self.courses_file, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                for row in reader:
                    courses.append(Course.from_csv_row(row))
        except FileNotFoundError:
            pass
        return courses

    def save_courses(self):
        with open(self.courses_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'trimester', 'credits', 'content', 'evaluation', 'grade'])
            for course in self.course_list:
                writer.writerow(course.to_csv_row())
