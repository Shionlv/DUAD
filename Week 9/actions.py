def get_integer(message):
    while True:
        try:
            value = int(input(message))
            if 0 <= value <= 100:
                return value
            else:
                print("Error: The grade must be between 0 and 100.")
        except ValueError:
            print("Error: You must enter a valid integer.")

def get_student_data(num_students):
    students = []
    for i in range(num_students):
        print(f"\nEntering data for student {i + 1}:")
        name = input("Enter the student's name: ")
        section = input("Enter the student's section (e.g., 11B): ")
        spanish_grade = get_integer("Enter the grade for Spanish: ")
        english_grade = get_integer("Enter the grade for English: ")
        social_studies_grade = get_integer("Enter the grade for Social Studies: ")
        science_grade = get_integer("Enter the grade for Science: ")
        student_info = {
            "name": name,
            "section": section,
            "grades": {
                "Spanish": spanish_grade,
                "English": english_grade,
                "Social Studies": social_studies_grade,
                "Science": science_grade
            }
        }
        students.append(student_info)
    return students

def display_students_data(students):
    if not students:
        print("\nNo student data available.")
        return
    print("\nStudent Data:")
    for student in students:
        print(f"Name: {student['name']}, Section: {student['section']}")
        print("Grades:")
        for subject, grade in student['grades'].items():
            print(f"  {subject}: {grade}")
        print("-")

def calculate_averages(students):
    if not students:
        print("\nNo student data available to calculate averages.")
        return
    total_general = 0
    for student in students:
        grades = student["grades"].values()
        average = sum(grades) / len(grades)
        total_general += average
        print(f"\n{student['name']} (Section {student['section']}) has an average of: {average:.2f}")
    overall_average = total_general / len(students)
    print(f"\nThe overall average of all students is: {overall_average:.2f}")

def show_top_students(students):
    if not students:
        print("\nNo student data available to determine the top 3.")
        return
    sorted_students = sorted(students, key=lambda x: sum(x['grades'].values()) / len(x['grades']), reverse=True)
    print("\nTop 3 Students with the Best Average Grades:")
    for i, student in enumerate(sorted_students[:3]):
        avg = sum(student['grades'].values()) / len(student['grades'])
        print(f"{i + 1}. {student['name']} (Section {student['section']}) - Average: {avg:.2f}")