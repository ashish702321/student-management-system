Student Management System

This project is a Student Management System built with Python's Tkinter library for the GUI and MySQL for the database. It allows users to manage student information including adding, updating, deleting, and viewing student records.

Features
Add new student records
Update existing student records
Delete student records
View all student records
Search for student records
User-friendly GUI
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x installed on your computer
MySQL server installed and running
Python libraries: tkinter, mysql-connector-python
Installation
Follow these steps to get the project up and running on your local machine:

Clone this repository:

sh
Copy code
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
Install the required Python libraries:

sh
Copy code
pip install mysql-connector-python
Set up the MySQL database:

Open MySQL command line or MySQL Workbench and create a new database:
sql
Copy code
CREATE DATABASE student_management;
USE student_management;
Create a table for storing student information:
sql
Copy code
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL
);
Update the database configuration in the project:

Open config.py (or the relevant file) and update the database connection details:
python
Copy code
db_config = {
    'host': 'localhost',
    'user': 'your-username',
    'password': 'your-password',
    'database': 'student_management'
}
Usage
To run the application, execute the following command:

sh
Copy code
python main.py
This will start the Tkinter application, and you can begin managing student records through the GUI.
