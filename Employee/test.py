"""
Program: test.py and employee.py
Author: Jessie Horvath
Date Modified: 03/29/2022

The purpose of these programs is to define an employee class with a 
function that will return a string containing the employee information.
The test file creates two employees and returns the output from the display
function.
"""
from employee import Employee

if __name__ == "__main__":
    e1 = Employee("Horvath", "Jessie", "123 Sesame St\nDes Moines, IA", "555-555-5555", True, "6/1/21", 600000)
    print(e1.display())

    e2 = Employee("Smith", "Peter", "34 Berry Ln\nChicago, IL", "123-321-4321", False, "3/1/21", 12.50)
    print(e2.display())