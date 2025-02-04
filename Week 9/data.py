import csv

def export_to_csv(students):
    if not students:
        print("\nNo student data available to export.")
        return
    filename = "students_data.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Section", "Spanish", "English", "Social Studies", "Science"])
        for student in students:
            writer.writerow([
                student['name'], student['section'], student['grades']['Spanish'], student['grades']['English'], 
                student['grades']['Social Studies'], student['grades']['Science']
            ])
    print(f"\nStudent data successfully exported to {filename}.")

def import_from_csv():
    filename = "students_data.csv"
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            students = []
            for row in reader:
                students.append({
                    "name": row[0], "section": row[1],
                    "grades": {"Spanish": int(row[2]), "English": int(row[3]), "Social Studies": int(row[4]), "Science": int(row[5])}
                })
            print("\nStudent data successfully imported from CSV.")
            return students
    except FileNotFoundError:
        print("\nNo previously exported file found. Please export data first.")
        return []