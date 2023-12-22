from colored import fg, attr, bg
import pandas as pd
from datetime import datetime
from prettytable import PrettyTable

# Function to save data to JSON file using pandas
def save_data(data):
    print("Data to be saved:")
    print(data)
    data.to_json("study_planner.json", orient="records", date_format="iso", indent=2)
    
    # Load the data again to ensure changes are applied
    return load_data()

# Function to load data from JSON file using pandas
def load_data():
    try:
        data = pd.read_json("study_planner.json", convert_dates=["due_date"])
    except FileNotFoundError:
        data = pd.DataFrame(columns=["name", "due_date", "type"])
    else:
        # Add 'type' column if it doesn't exist
        if 'type' not in data.columns:
            data['type'] = ""
    print("Loaded Data:")
    print(data)
    return data

# Function to add a new task such as class, assignment, or exam
def add_task(data, task_type):
    name = get_user_input("Enter the name of the {}: ".format(task_type))
    due_date = get_valid_date_input("Enter the due date (DD/MM/YYYY): ")

    # Format the due date to "DD/MM/YYYY" before saving
    due_date_str = due_date.strftime("%d/%m/%Y")

    task = pd.DataFrame({"name": [name], "due_date": [due_date_str], "type": [task_type]})
    data = pd.concat([data, task], ignore_index=True)
    
    # Save the data immediately and load it back
    data = save_data(data)
    
    print("{} added successfully!".format(task_type.capitalize()))

# Function to edit a task such as class, assignment, or exam
def edit_task(data, task_type):
    print("List of {}: {}".format(task_type, data[data["type"] == task_type]["name"].tolist()))
    task_name = input("Enter the name of the {} to edit: ".format(task_type))

    for index, task in data[data["type"] == task_type].iterrows():
        if task["name"] == task_name:
            new_name = input("Enter the new name (press Enter to keep the same): ")
            new_due_date_str = input("Enter the new due date (DD/MM/YYYY) (press Enter to keep the same): ")

            if new_name:
                data.at[index, "name"] = new_name
            if new_due_date_str:
                try:
                    new_due_date = datetime.strptime(new_due_date_str, "%d/%m/%Y")
                    data.at[index, "due_date"] = new_due_date.strftime("%d/%m/%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
                    return

            save_data(data)
            print("{} edited successfully!".format(task_type.capitalize()))
            return

    print("{} not found!".format(task_type.capitalize()))

# Function to delete a task such as class, assignment, or exam
def delete_task(data, task_type):
    print("List of {}: {}".format(task_type, data[data["type"] == task_type]["name"].tolist()))
    task_name = input("Enter the name of the {} to delete: ".format(task_type))

    # Convert task name to string and strip leading and trailing whitespaces, and make the comparison case-insensitive
    task_name = str(task_name).strip().lower()

    for index, task in data[data["type"] == task_type].iterrows():
        if str(task["name"]).strip().lower() == task_name:
            data = data.drop(index, axis=0).reset_index(drop=True)
            save_data(data)
            print("{} deleted successfully!".format(task_type.capitalize()))
            return

    print("{} not found!".format(task_type.capitalize()))

# Function to check all tasks
def check_all_tasks(data):
    today = datetime.today().date()

    if not data.empty and 'due_date' in data.columns:
        print("\nAll Tasks:")
        task_subset = data[pd.to_datetime(data["due_date"]).dt.date > today]

        if not task_subset.empty:
            for _, task in task_subset.iterrows():
                print(f"{task['name']} ({task['type'].capitalize()}) - Due on {task['due_date'].strftime('%d/%m/%Y')}")
        else:
            print("No upcoming tasks!")
    else:
        print("There is nothing to check!")

# Function to get user input
def get_user_input(prompt):
    return input(prompt)

# Function to get valid date input
def get_valid_date_input(prompt):
    while True:
        date_str = get_user_input(prompt)
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            print("Sorry! Please enter the date as DD/MM/YYYY. Try again.")

# Main function
def main():
    data = load_data()
    
    while True:
        print(f"{fg('white')}{bg('black')}\nStudy Planner Menu{attr('reset')}")
        print(f"{fg('blue')}{bg('black')}1. Add Class")
        print("2. Add Assignment")
        print("3. Add Exam")
        print("4. Edit Class")
        print("5. Edit Assignment")
        print("6. Edit Exam")
        print("7. Delete Class")
        print("8. Delete Assignment")
        print("9. Delete Exam")
        print("10. Check All Tasks")
        print(f"{fg('white')}{bg('black')}0. Exit")

        choice = get_user_input("Enter your choice (0-10): ")

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
            check_all_tasks(data)
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")
        
        data = load_data()

if __name__ == "__main__":
    main()