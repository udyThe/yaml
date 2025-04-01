import yaml

def load_data(file_path):
    """
    Load data from a YAML file.

    :param file_path: Path to the YAML file.
    :return: Data loaded from the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)  # Load YAML file as a Python dictionary
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

def display_students(students):
    """
    Display information about all students.

    :param students: List of student dictionaries.
    """
    print("\nAll Students:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")

def filter_students_by_gpa(students, min_gpa):
    """
    Filter and display students with a GPA above the specified minimum.

    :param students: List of student dictionaries.
    :param min_gpa: Minimum GPA for filtering.
    """
    filtered_students = [s for s in students if s['gpa'] >= min_gpa]

    print(f"\nStudents with GPA >= {min_gpa}:")
    if filtered_students:
        for student in filtered_students:
            print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")
    else:
        print("No students found.")

def main():
    # Load the data from the YAML file
    file_path = 'students.yaml'
    data = load_data(file_path)

    if data and 'students' in data:
        students = data['students']

        # Display all students
        display_students(students)

        # Filter students by GPA
        try:
            min_gpa = float(input("\nEnter minimum GPA to filter students: "))
            filter_students_by_gpa(students, min_gpa)
        except ValueError:
            print("Invalid input! Please enter a valid GPA.")
    else:
        print("No valid student data found.")

if __name__ == "__main__":
    main()
