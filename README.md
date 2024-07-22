# GradeBook Application

This GradeBook Application allows teachers to manage courses and student registrations, and students to view courses, take tests, and view their transcripts. The application is built using Python and leverages Object-Oriented Programming (OOP) concepts, CSV file handling, and tabulate for displaying data in a tabular format.

## Features

### Teacher Menu
- **Add Student**: Add a new student to the GradeBook.
- **Add Course**: Add a new course with a URL for lesson content and a set of 5 multiple-choice questions.
- **Register Student for Course**: Register a student for a specific course.
- **Calculate GPA**: Calculate the GPA for a specific student.
- **Calculate Ranking**: Display student rankings by GPA.
- **Search by Grade**: Search for students who have received a specific grade.
- **Generate Transcript**: Generate and display the transcript for a specific student.

### Student Menu
- **View Courses**: View courses the student is enrolled in.
- **Learn Course Content**: View the content URL for the courses the student is enrolled in.
- **Take Test**: Attempt the multiple-choice questions for a specific course and receive a grade.
- **View Transcript**: View the student's transcript, including courses taken and GPA.

## Getting Started

### Prerequisites
- Python 3.x
- `tabulate` library (install via `pip install tabulate`)

### Files
- `main.py`: Main entry point of the application.
- `gradebook.py`: Contains the `GradeBook`, `Student`, and `Course` classes.

### Running the Application
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required libraries:
    ```sh
    pip install tabulate
    ```
4. Run the application:
    ```sh
    python main.py
    ```

### CSV Files
- `students.csv`: Stores student information.
- `courses.csv`: Stores course information.

## Usage

### Teacher Menu
1. **Add Student**:
    - Enter student email and names.
2. **Add Course**:
    - Enter course name, trimester, credits, content URL, multiple-choice questions, and grade.
3. **Register Student for Course**:
    - Enter student email and course name.
4. **Calculate GPA**:
    - Enter student email to calculate and display the GPA.
5. **Calculate Ranking**:
    - Display student rankings by GPA.
6. **Search by Grade**:
    - Enter grade to search for students with that grade.
7. **Generate Transcript**:
    - Enter student email to generate and display the transcript.

### Student Menu
1. **View Courses**:
    - View courses the student is enrolled in.
2. **Learn Course Content**:
    - View the content URL for the courses the student is enrolled in.
3. **Take Test**:
    - Attempt the multiple-choice questions for a specific course and receive a grade.
4. **View Transcript**:
    - View the student's transcript, including courses taken and GPA.

