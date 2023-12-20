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