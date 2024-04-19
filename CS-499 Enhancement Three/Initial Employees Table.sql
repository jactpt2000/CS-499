-- ----------------------------------------------------------------------------------
-- Name: Jorge Argueta
-- Class: DAD220
-- Date: 4/6/2024
--
-- Description: This script sets up the 'DAD220' database and populates it with
-- employee and department data. It creates tables, inserts data, and performs
-- basic queries to demonstrate SQL functionality. This structured SQL script
-- serves to illustrate database setup, data manipulation, and querying techniques.
-- ----------------------------------------------------------------------------------

-- Create the DAD220 database if it does not already exist
CREATE DATABASE DAD220;

-- Use the newly created DAD220 database for all subsequent operations
USE DAD220;

-- Create the Employee table with fields suitable for storing detailed employee information
CREATE TABLE Employee (
    Employee_ID SMALLINT,  -- Unique identifier for each employee
    First_Name VARCHAR(40),  -- Employee's first name
    Last_Name VARCHAR(60),  -- Employee's last name
    Department_ID SMALLINT,  -- Identifier linking employees to their respective departments
    Classification VARCHAR(10),  -- Employee classification (e.g., Exempt, Non-Exempt)
    Status VARCHAR(10),  -- Current employment status (e.g., Full-Time, Part-Time)
    Salary DECIMAL(7,2)  -- Salary amount with precision for cents
);

-- Create the Branches table to maintain information about different departments
CREATE TABLE Branches (
    Department_ID SMALLINT,  -- Unique identifier for each department
    Department_Name VARCHAR(50)  -- Descriptive name of the department
);

-- Populate the Employee table with initial data
INSERT INTO Employee(Employee_ID,First_Name,Last_Name,Department_ID,Classification,Status,Salary)
VALUES
    (100,'John','Smith',1,'Exempt','Full-Time',90000),
    (101,'Mary','Jones',2,'Non-Exempt','Part-Time',35000),
    (102,'Mary','Williams',3,'Exempt','Full-Time',80000),
    (103,'Gwen','Johnson',2,NULL,'Full-Time',40000),
    (104,'Michael','Jones',3,'Non-Exempt','Full-Time',90000);

-- Display all employee records to verify insertion and check table contents
SELECT *
FROM Employee;

-- Insert department data into the Branches table
INSERT INTO Branches(Department_ID,Department_Name)
VALUES
    (1,'Accounting'),
    (2,'Human Resources'),  -- Corrected the previous typo 'Resaurces' to 'Resources'
    (3,'Information Systems'),
    (4,'Marketing');

-- Query to calculate and display the total salary expenditure for the Information Systems department
SELECT SUM(Salary)
FROM Employee
WHERE Department_ID = 3;

-- Retrieve and display all employees who are not classified as 'Exempt'
SELECT *
FROM Employee
WHERE Classification <> 'Exempt';

-- Determine and display the highest salary present among all employees
SELECT MAX(Salary)
FROM Employee;
