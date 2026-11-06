# Expense Tracker | Personal Finance Management System

## Project Overview
Expense Tracker is a Python-based desktop application developed using Tkinter. It helps users manage their personal finances by recording income and expenses, tracking balances, and analyzing financial transactions.

## Features

- Add Income and Expense transactions.
- Select transaction categories.
- View total income, total expenses, and net balance.
- View all transactions in one place.
- Separate Income and Expenses pages.
- Filter transactions by date range.
- Filter transactions by category.
- Export transaction records to CSV files.
- Delete selected transactions.
- Analytics dashboard for financial summaries.
- Refresh transaction data.
- Create transaction backups.
- Input validation for dates and amounts.
- Automatically save transaction records locally.

## Technologies Used

- Python
- Tkinter (GUI)
- CSV (Data Storage)
- Python CSV Module
- DateTime Module

## Categories

- Food
- Travel
- Bills
- Shopping
- Other

## Calculation Logic

**Total Income:** Sum of all income transactions.

**Total Expenses:** Sum of all expense transactions.

**Net Balance:**

Net Balance = Total Income - Total Expenses

## Input Validation

- All required fields must be completed.
- Date must follow YYYY-MM-DD format.
- Amount must be a valid number.
- Amount must be greater than zero.

## Data Storage

All transaction records are stored locally in transactions.csv.

The application also supports exporting records to CSV files and creating backup copies.

## How to Run

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

python main.py


## Project Structure

text
Expense_Tracker/
│
├── main.py
├── transactions.csv
├── transactions_backup.csv
└── README.md


## Sample Report

| Transaction Type | Amount |
|---|---:|
| Total Income | Rs. 50,000 |
| Total Expenses | Rs. 15,000 |
| Net Balance | Rs. 35,000 |

*Sample values are for demonstration purposes.*

## Conclusion

Expense Tracker provides a simple and user-friendly way to manage personal finances. It helps users monitor income, control expenses, and maintain transaction records efficiently.

## Developer

**Developed by:** Kiran 

**Project:** Expense Tracker

**Internship Organization:** CodeNova

**Programming Language:** Python

**Project Type:** Desktop Application

## Acknowledgement

This project was developed as part of the CodeNova internship program to practice Python programming, GUI development, file handling, and financial data management.