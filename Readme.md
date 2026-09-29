# TRIPWISE: Smart Travel Planning and Budget Management System

## 1. Overview

TRIPWISE is a Python-based command-line travel planning and budget management system developed for the course Introduction to Problem Solving and Programming (CSE-1021).

The project helps users organize a trip by setting up trip details, creating a day-wise itinerary, planning the budget, detecting time conflicts, managing group expenses, and viewing a final trip summary.

## 2. Features

* Trip Setup – Enter destination, trip duration, number of travellers, trip type, and total budget.
* Itinerary Planning – Add activities for each day with place, start time, and end time.
* Budget Planning – Manage expenses under Transport, Stay, Food, Activities, and Miscellaneous.
* Time-Conflict Detection – Check whether activities scheduled on the same day overlap.
* Group Expense Management – Record payments made by travellers and calculate fair shares and settlements.
* Trip Summary – Display trip details, itinerary, budget status, and time-conflict results.
* nput Validation – Handles invalid inputs such as negative values, invalid times, and empty activity/place names.

## 3. Technologies / Tools Used

* Programming Language: Python 3
* Development Environment: Visual Studio Code / Python IDLE
* Version Control: Git and GitHub
* Interface: Command-Line Interface (CLI)
* Libraries: Python standard library only

## 4. Project Structure


TRIPWISE/
│
├── main.py
├── trip.py
├── itinerary.py
├── budget.py
├── conflicts.py
├── group_expenses.py
├── report.py
├── utils.py
├── statement.md
├── README.md
└── .gitignore

### Module Description

| File                | Purpose                                                         |
| ------------------- | --------------------------------------------------------------- |
| `main.py`           | Main program and menu control                                   |
| `trip.py`           | Handles basic trip information                                  |
| `itinerary.py`      | Creates and displays the trip itinerary                         |
| `budget.py`         | Handles budget categories and calculations                      |
| `conflicts.py`      | Detects overlapping activities                                  |
| `group_expenses.py` | Calculates group expense sharing and settlements                |
| `report.py`         | Displays the complete trip summary                              |
| `utils.py`          | Provides common utility functions                               |
| `statement.md`      | Problem statement, scope, target users, and high-level features |
| `README.md`         | Project documentation                                           |
| `.gitignore`        | Lists files that should not be uploaded to Git                  |

## 5. Requirements

* Python 3.x
* VS Code, Python IDLE, or another Python-compatible IDE
* Git/GitHub for version control

No external Python packages are required.

## 6. Installation and Running the Project

### Step 1: Clone the repository


git clone < https://github.com/adhirad2707-ux/TRIPWISE1.git >


### Step 2: Open the project folder

Open the `TRIPWISE` folder in VS Code or another Python IDE.

### Step 3: Run the program

python main.py


If your system uses `python3`:


python3 main.py


## 7. How to Use

1. Run `main.py`.
2. Enter the required trip details.
3. Select options from the main menu.
4. Create a day-wise itinerary.
5. Enter the planned budget and expenses.
6. Check the itinerary for time conflicts.
7. Enter group payments if travelling with multiple people.
8. View the final trip summary.
9. Exit the program.

## 8. Testing Instructions

### Test 1: Valid Trip Details

Enter valid destination, duration, number of travellers, trip type, and budget.

Expected Result: Trip details are accepted and stored.

### Test 2: Budget Validation

Enter valid positive budget and expense amounts.

Expected Result: The system calculates total expenses and remaining budget.

### Test 3: Invalid Budget Input

Enter a negative value or invalid text where a positive number is required.

Expected Result: The program rejects the input and asks for a valid value.

### Test 4: Time Conflict

Add two activities on the same day whose time periods overlap.

Expected Result: The system reports a time conflict.

### Test 5: No Time Conflict

Add activities with non-overlapping time periods.

Expected Result: The system reports that there are no conflicts.

### Test 6: Group Expenses

Enter payments made by different travellers.

Expected Result: The program calculates the total expense, fair share, and required settlements.

### Test 7: Invalid Activity Details

Enter an empty place/activity name or invalid time.

Expected Result: The program asks the user to enter valid information.

## 9. Screenshots

Screenshots can be added here to demonstrate:

* Main menu
* Trip setup
* Itinerary
* Budget planning
* Time-conflict detection
* Group expense calculation
* Final trip summary

## 10. Limitations

* The project is currently command-line based.
* Trip information is handled during program execution and is not stored in a database.
* It does not use live travel information such as real-time flight, hotel, or weather data.

## 11. Future Enhancements

* GUI/web interface
* Database-based trip storage
* Real-time weather and travel information
* Map and route integration
* Hotel and transport recommendations
* Exporting trip plans and reports
* User accounts and authentication

## 12. Project Purpose

TRIPWISE demonstrates fundamental Python programming and problem-solving concepts, including functions, conditional statements, loops, lists, dictionaries, input validation, modular programming, and basic algorithmic thinking.
