

def show_menu():
    print("\nMenu:")
    print("1. Enter student data")
    print("2. Display student data")
    print("3. Show the top 3 students with the best average grade")
    print("4. Show the average grade of all students")
    print("5. Export data to CSV")
    print("6. Import data from CSV")
    print("7. Exit")
    while True:
        try:
            option = int(input("Enter the number of the option you want to select: "))
            if 1 <= option <= 7:
                return option
            else:
                print("Error: Please select a valid option (1-7).")
        except ValueError:
            print("Error: You must enter a valid integer.")
