import menu  
import actions
import data

def main():
    students = []

    while True:
        option = menu.show_menu()

        if option == 1:
            num_students = actions.get_integer("\nPlease enter the number of students: ")
            students.extend(actions.get_student_data(num_students))

        elif option == 2:
            actions.display_students_data(students)

        elif option == 3:
            actions.show_top_students(students)

        elif option == 4:
            actions.calculate_averages(students)

        elif option == 5:
            data.export_to_csv(students)

        elif option == 6:
            imported_students = data.import_from_csv()
            if imported_students:
                students = imported_students

        elif option == 7:
            print("\nExiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()