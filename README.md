# Budget Tracker (PostgreSQL)

A command-line budget tracking application built with Python and PostgreSQL.

## Overview

This project was built to strengthen my understanding of backend development fundamentals, including Python, PostgreSQL, database operations, input validation, and version control with Git/GitHub.

The application allows users to manage expenses through a menu-driven interface while storing all data in a PostgreSQL database.

## Features

* Add expenses
* View all expenses
* Calculate total expenses
* Calculate category-wise expense totals
* Update existing expenses
* Delete expenses
* Input validation for categories, amounts, and IDs
* Persistent storage using PostgreSQL

## Technologies Used

* Python
* PostgreSQL
* Psycopg
* Git & GitHub
* Environment Variables (`.env`)

## Project Structure

The application follows a simple backend-oriented architecture:

Database Connection
→ Cursor Operations
→ Business Logic Functions
→ Main Menu Controller

Core functions:

* `add_expenses()`
* `view_expenses()`
* `calculate_total()`
* `calculate_category_total()`
* `update_expenses()`
* `delete_expenses()`
* `main_menu()`

The `main_menu()` function acts as the entry point and connects all application features. The program runs continuously until the user chooses to exit.

## Database Operations Implemented

This project implements complete CRUD operations:

### Create

* Add new expenses

### Read

* View expenses
* Calculate totals
* Calculate category totals

### Update

* Modify existing expenses by ID

### Delete

* Remove expenses by ID

## Learning Outcomes

Through this project, I gained practical experience with:

* Python functions and program structure
* Input validation and exception handling
* SQL queries (`INSERT`, `SELECT`, `UPDATE`, `DELETE`, `GROUP BY`, `SUM`)
* PostgreSQL integration using Psycopg
* Git and GitHub workflows
* Environment variable management for sensitive credentials
* Designing and building a complete CRUD application
