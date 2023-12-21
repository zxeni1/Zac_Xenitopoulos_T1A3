# Function to load data from JSON file
import json
from datetime import datetime, timedelta

def load_data():
    try:
        with open("study_planner.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"classes": [], "assignments": [], "exams": []}
    return data

#  Function to save data to JSON file 
def save_data(data):
    with open("study_planner.json", "w") as file:
        json.dump(data, file, indent=2)

#function to add a new task such as class, assignment or exam
def get_user_input(prompt):
    return input(prompt)

def get_valid_date_input(prompt):
    while True:
        date_str = get_user_input(prompt)
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            print("Sorry! Please enter the date as DD/MM/YYYY. Try again.")

def add_task(data, task_type):
    name = get_user_input("Enter the name of the {}: ".format(task_type))
    due_date = get_valid_date_input("Enter the due date (DD/MM/YYYY): ")

    task = {"name": name, "due_date": due_date.strftime("%d/%m/%Y")}
    data[task_type].append(task)
    save_data(data)
    print("{} added successfully!".format(task_type.capitalize()))


# Function to edit a task such as class, assignment or exam
def edit_task(data, task_type):
    print("List of {}: {}".format(task_type, [task["name"] for task in data[task_type]]))
    task_name = input("Enter the name of the {} to edit: ".format(task_type))

    for task in data[task_type]:
        if task["name"] == task_name:
            new_name = input("Enter the new name (press Enter to keep the same): ")
            new_due_date_str = input("Enter the new due date (DD/MM/YYYY) (press Enter to keep the same): ")

            if new_name:
                task["name"] = new_name
            if new_due_date_str:
                try:
                    task["due_date"] = datetime.strptime(new_due_date_str, "%d/%m/%Y").strftime("%d/%m/%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
                    return

            save_data(data)  # Fix: Adjusted the indentation of this line
            print("{} edited successfully!".format(task_type.capitalize()))
            return

    print("{} not found!".format(task_type.capitalize()))

# Function to delete a task such as class, assignment or exam
def delete_task(data, task_type):
    print("List of {}: {}".format(task_type, [task["name"] for task in data[task_type]]))
    task_name = input("Enter the name of the {} to delete: ".format(task_type))

    for task in data[task_type]:
        if task["name"] == task_name:
            data[task_type].remove(task)
            save_data(data)
            print("{} deleted successfully!".format(task_type.capitalize()))
            return

    print("{} not found!".format(task_type.capitalize()))

# Function to check reminders for classes
def check_class_reminders(data):
    today = datetime.today().date()
    upcoming_classes = []

    for task in data["classes"]:
        due_date = datetime.strptime(task["due_date"], "%d/%m/%Y").date()
        if today < due_date:
            upcoming_classes.append((task["name"], due_date))

    if upcoming_classes:
        print("\nUpcoming Classes:")
        for class_name, due_date in sorted(upcoming_classes, key=lambda x: x[1]):
            print("{} - On {}".format(class_name, due_date))
    else:
        print("\nNo upcoming classes!")

# Function to check reminders for assignments and exams
def check_exam_assignment_reminders(data):
    today = datetime.today().date()
    upcoming_tasks = []

    for task_type in ["assignments", "exams"]:
        for task in data[task_type]:
            due_date = datetime.strptime(task["due_date"], "%d/%m/%Y").date()
            if today < due_date:
                upcoming_tasks.append((task["name"], due_date, task_type))
    
    if upcoming_tasks:
        print("\nUpcoming {}:".format("Exams and Assignments"))
        for task_name, due_date, task_type in sorted(upcoming_tasks, key=lambda x: x[1]):
            print("{} ({}) - Due on {}".format(task_name, task_type.capitalize(), due_date))
    else:
        print("\nNo upcoming exams or assignments!")

def check_all_tasks(data):
    print("\nAll Tasks:")
    for task_type in ["classes", "assignments", "exams"]:
        print("\n{}:".format(task_type.capitalize()))
        for task in data[task_type]:
            print("{} - Due on {}".format(task["name"], task["due_date"]))

def main():
    data = load_data()

    while True:
        print("\nStudy Planner Menu:")
        print("1. Add Class")
        print("2. Add Assignment")
        print("3. Add Exam")
        print("4. Edit Class")
        print("5. Edit Assignment")
        print("6. Edit Exam")
        print("7. Delete Class")
        print("8. Delete Assignment")
        print("9. Delete Exam")
        print("10. Check Class Reminders")
        print("11. Check Exam and Assignment Reminders")
        print("12. Check All")
        print("0. Exit")

        choice = get_user_input("Enter your choice (0-12): ")

        if choice == "0":
            break
        elif choice == "1":
            add_task(data, "classes")
        elif choice == "2":
            add_task(data, "assignments")
        elif choice == "3":
            add_task(data, "exams")
        elif choice == "4":
            edit_task(data, "classes")
        elif choice == "5":
            edit_task(data, "assignments")
        elif choice == "6":
            edit_task(data, "exams")
        elif choice == "7":
            delete_task(data, "classes")
        elif choice == "8":
            delete_task(data, "assignments")
        elif choice == "9":
            delete_task(data, "exams")
        elif choice == "10":
            check_class_reminders(data)
        elif choice == "11":
            check_exam_assignment_reminders(data)
        elif choice == "12":
            check_all_tasks(data)
        else:
            print("Invalid choice. Please enter a number between 0 and 12.")

if __name__ == "__main__":
    main()
