# Help Document - Study Planner 

Study Planner is a command-line tool made to assist you in effectively planning and managing your study obligations. To install, set up, and utilise the application, follow the instructions below.

## Step 1. Installation



Clone the repository to your local machine using the following command:

```bash
git clone git@github.com:zxeni1/Zac_Xenitopoulos_T1A3.git
```

## Step 2. Execute the Setup Script

By running the setup script that comes with this code, it will check if python is installed and or updated, (if not, prompt you to install) set up a virtual environment, install the necessary packages, run the appilcation then finally deactivate the virtual environment. 

```bash
./src/run.sh
```

## Dependencies
The application relies on the following Python packages, which are automatically installed during the setup process:

- colored
- pandas
- prettytable

## System/Hardware Requirements

Study Planner is a lightweight application with minimal system requirements. Ensure that you have a stable internet connection for the setup process.

## Features 

### Task Management
Classes, homework, and tests can be added, edited, and deleted. Enter the assignment's name and due date.

### Persistence of Data
A JSON file called study_planner.json is where the data is loaded and stored. Make sure the application and the file are in the same directory.

### Future Task Checker
Using the current date as a basis, check and show forthcoming tasks.provide details on the names, kinds, and deadlines of the tasks.

Enjoy using Study Planner for efficient task management!


