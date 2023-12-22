# Zac_Xenitopoulos_T1A3

## Q1 Provide full attribution to referenced sources (where applicable).

The following modules and libraries are used by the code that is provided:

- **colored library:** A Python library for adding color to terminal text. [Link to colored library](https://pypi.org/project/colored/)
- **pandas library:** A powerful data manipulation and analysis library. [Link to pandas library](https://pandas.pydata.org/)
- **datetime module:** A module in the Python standard library for working with dates and times. [Link to datetime module](https://docs.python.org/3/library/datetime.html)
- **PrettyTable module:** A simple Python library for creating ASCII tables. [Link to prettytable module](https://pypi.org/project/prettytable/)

Extral referencing was used from [Python cheat sheet](https://www.pythoncheatsheet.org/) on a frequient basis to help with troubleshooting and the general operation of my application. 

A large variety of different tutorials were also used in the progess of developing my application from [w3schools - python](https://www.w3schools.com/python/). In conjunction with the above mentioned, these resources, libraries and modules helped develope a running application. 

## Q2 Provide a link to your source control repository
### My Github Repo: [Click Here!!](https://github.com/zxeni1/Zac_Xenitopoulos_T1A3)

## Q3 Identify any code style guide or styling conventions that the application will adhere to.

The code adheres to Python's PEP 8 style guide. The code complies with the following elements of the style guide

- **Imports:** The script starts with a structured list of imports. Standard library imports come before third-party imports, and each import is on its own line.

- **Whitespace in Expressions and Statements:** The code is easy to read since it consistently employs whitespace in expressions and statements.

- **Comments:** Comments are a useful tool for clarifying the intent behind methods and important code sections. Clear and succinct, inline comments offer clarification.

- **Function and Variable Names:** Following the snake_case naming pattern, function and variable names are descriptive. As a result, the code is easier to read and comprehend.

- **Indentation:** The code follows PEP 8's suggested style by using four spaces for indentation.

- **String Formatting:** A clear and effective method for string formatting is to utilise f-strings.

It is important that following a particular style guide—like PEP 8—improves the readability and maintainability of code. Additionally, developers may work together more easily on projects when code styles are consistent.

## Q4 Develop a list of features that will be included in the application

### 1. Managing Tasks:

This feature gives users multiple methods to interact with their tasks. With a name and a deadline, users can add new tasks (such classes, assignments, or tests). The programme uses variables to keep track of each task's name, due date, and kind (exam, assignment, or class). The application uses variables to ensure that task details are properly kept and available, demonstrating a mastery of the idea of variable scope. Loops are employed for task iteration, and conditional control structures manage user selections to guarantee that the right actions are performed in response to user input.

### 2. Persistence of Data:

The programme loads and saves data from a *"study_planner.json"* JSON file to guarantee that user data is preserved across sessions. This file contains the task data that the programme tries to load when it launches. In the event that the file cannot be located (FileNotFoundError), the application first constructs an empty DataFrame. Within the application, variables are used to store the loaded data. To guarantee that changes are maintained between programme executions, the data is saved back to the JSON file following each alteration. This illustrates how variables are used and how much flexibility they provide for managing data in an application.

### 3. Upcoming Task verification:

This function looks for all upcoming jobs based on the current date and shows them all. The datetime module is used by the programme to get the current date. The due dates of the jobs kept in the DataFrame are then compared to this date. The application prints out task details, including names, types, and due dates, if tasks with future dates are discovered. To handle situations when tasks are imminent or not, conditional control structures are used. In instances when the "due_date" column cannot be located in the DataFrame, error handling is used to handle the issue graciously and notify the user. A thorough grasp is demonstrated by the usage of variables, loops, conditional control structures, and error handling.

## Q5 Develop an implementation plan

![alt text for screen readers](/docs/2.jpg)
![alt text for screen readers](/docs/3.jpg)
![alt text for screen readers](/docs/5.jpg)
![alt text for screen readers](/docs/6.jpg)
![alt text for screen readers](/docs/7.jpg)
![alt text for screen readers](/docs/8.jpg)
![alt text for screen readers](/docs/9.jpg)
![alt text for screen readers](/docs/10.jpg)
![alt text for screen readers](/docs/1.jpg)
![alt text for screen readers](/docs/4.jpg)
## Q6 Help Document

To view the help document please click on the link below!

### [Click me!](Help.md)