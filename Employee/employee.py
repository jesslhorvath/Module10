"""
Program: test.py and employee.py
Author: Jessie Horvath
Date Modified: 03/29/2022

The purpose of these programs is to define an employee class with a 
function that will return a string containing the employee information.
The test file creates two employees and returns the output from the display
function.
"""
class Employee:
    # Constructor
    def __init__(self, lname, fname, address, phone_number, salaried, start_date, salary):
        if salaried == True:
            salary = "Salaried: $" + str(salary) + "/year"
        else:
            salary = "Hourly Employee: $" + str(salary) + "/hour"

        self.last_name = lname
        self.first_name = fname
        self._address = address
        self.phone = phone_number
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname
    
    def set_address(self, address):
        self._address = address
    
    def set_phone(self, phone):
        self.phone_number = phone

    def set_salaried_status(self, salaried):
        self._salaried = salaried

    def set_start(self, date):
        self._start_date = date

    def set_salary(self, salary):
        self._salary = salary

    def display(self):
        return str(self.first_name) + " " + str(self.last_name) + "\n" + str(self._address) + "\n" + str(self.phone) + "\n" + str(self._salary) + "\n" + "Start Date: " + str(self._start_date)