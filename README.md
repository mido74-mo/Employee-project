# Employees System

A console-based employee management application designed for factory HR operations. Built with Object-Oriented Programming principles.

---

## Overview

This program provides a simple menu-driven interface to manage employee records. It supports adding employees, listing all records, deleting employees by age range, updating salaries by name, and exiting the application.

---

## Features

| Option | Feature | Description |
|--------|---------|-------------|
| 1 | Add new employee | Register an employee with name, age, and salary |
| 2 | List all employees | Display all registered employees in a formatted list |
| 3 | Delete by age range | Remove all employees whose age falls within a specified range |
| 4 | Update salary by name | Modify an employee's salary using their full name |
| 5 | Exit program | Terminate the application |

---

## Architecture

The project follows an OOP design with three main classes:

### `Employee`
- Holds individual employee data: name, age, and salary
- Provides basic data access and display functionality

### `EmployeeManager`
- Maintains the collection of `Employee` objects
- Implements core business logic for all CRUD operations:
  - Adding employees to the system
  - Retrieving and displaying the employee list
  - Filtering and removing employees by age range
  - Searching and updating employee salaries by name

### `FrontendManager`
- Handles all user interface interactions
- Displays the program menu and options
- Validates user input (ensures choice is an integer from 1 to 5)
- Routes valid choices to the appropriate `EmployeeManager` methods

---

## Input Validation

The program enforces strict input validation:

- **Menu choice**: Must be an integer between 1 and 5
  - Out-of-range values prompt: `"Invalid range. Try again!"`
  - Non-integer values prompt: `"Invalid input. Try again!"`
  - The menu reappears until valid input is provided
- **Employee data**: Age and salary must be integers
- **Name handling**: Supports full names including spaces (e.g., `"Belal Mostafa"`)

---

## Usage Example
