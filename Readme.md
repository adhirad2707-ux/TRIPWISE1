TRIPWISE: A Smart Travel Planning and Budget Management System

Overview

TRIPWISE is a Python-based command-line travel planning and budget management system. It helps users organize a trip by creating a day-wise itinerary, planning a travel budget, detecting overlapping activities, splitting group expenses, and viewing a complete trip summary.

The project is developed for Introduction to Problem Solving and Programming (CSE-1021) and uses Python concepts such as input/output, loops, conditional statements, functions, lists, dictionaries, arithmetic operations, validation, and modular programming.

Features

Trip setup with destination, duration, travellers, trip type, and budget

Day-wise itinerary planning

Budget planning for Transport, Stay, Food, Activities, and Miscellaneous expenses

Total expense and budget-status calculation

Time-conflict detection for overlapping activities

Group expense splitting and fair-share calculation

Complete trip summary

Input validation for important user inputs

Technologies / Tools Used

Python 3

VS Code or any Python-compatible editor

Command Line / Terminal

Git and GitHub

No external Python libraries are required

Project Structure

TRIPWISE/
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

Module Description

main.py – Main menu and overall program control

trip.py – Trip information and input validation

itinerary.py – Day-wise itinerary creation

budget.py – Budget categories and calculations

conflicts.py – Activity time-overlap detection

group_expenses.py – Group expense calculations

report.py – Complete trip summary

utils.py – Utility functions

Installation & Running

Requirements

Python 3.8 or newer is recommended

VS Code or another Python-compatible editor

No additional packages are required

Steps

Download or clone the TRIPWISE GitHub repository.

Open the project folder in VS Code or a terminal.

Make sure all Python files are in the same folder.

Check Python installation:

python --version

Run the project:

python main.py

On some Windows systems:

py main.py

How to Use

After running main.py, enter the trip details and use the main menu:

Create / Update Itinerary

Plan Budget

Check Time Conflicts

Split Group Expenses

View Complete Trip Summary

Exit

Enter the requested information for each selected option and review the generated results.

Testing Instructions

The project can be tested manually through the command line.

Budget Testing

Enter a budget greater than total estimated expenses → Within entered budget

Enter a budget equal to total estimated expenses → Budget exactly used

Enter a budget lower than total estimated expenses → Budget exceeded

Time-Conflict Testing

Add two activities with overlapping times on the same day → The conflict should be displayed.

Add activities with non-overlapping times → No time conflicts found.

Group Expense Testing

Enter different amounts paid by multiple travellers.

Expected result: The program calculates total spending, fair share per traveller, and who needs to pay or receive money.

Input Validation Testing

Try invalid numeric values or invalid time formats.

Expected result: The program rejects invalid input and asks for valid information.

Screenshots

Screenshots are optional but recommended.

Suggested screenshots to add:

Main menu

Trip setup

Itinerary

Budget summary

Time-conflict detection

Group expense splitting

screenshots can be stored in a screenshots/ folder and added to this README using Markdown image syntax.