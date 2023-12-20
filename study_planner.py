import json
from datetime import datetime, timedelta

def load_data():
    try:
        with open("study_planner.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"classes": [], "assignments": [], "exams": []}
    return data

def save_data(data):
    with open("study_planner.json", "w") as file:
        json.dump(data, file, indent=2)

def add_task(data, task_type):
    name = input("Enter the name of the {}: ".format(task_type))
    due_date_str = input("Enter the due date (DD/MM/YYYY): ")
    
    try:
        due_date = datetime.strptime(due_date_str, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
        return
    
    task = {"name": name, "due_date": due_date.strftime("%d/%m/%Y")}

    data[task_type].append(task)
    save_data(data)
    print("{} added successfully!".format(task_type.capitalize()))

def edit_task(data, task_type):
    print("List of {}: {}".format(task_type, [task["name"] for task in data[task_type]]))
    task_name = input("Enter the name of the {} to edit: ".format(task_type))