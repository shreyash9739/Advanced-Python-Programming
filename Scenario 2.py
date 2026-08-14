class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def categorize(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print("\nEmployee Information")
        print("--------------------")

        for employee in self.employees:
            print("Employee ID :", employee.employee_id)
            print("Name        :", employee.name)
            print("Salary      :", employee.salary)
            print("Category    :", employee.categorize())
            print("--------------------")


company = Company()

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEnter details of Employee", i + 1)
    employee_id = input("Employee ID: ")
    name = input("Name: ")
    salary = float(input("Salary: "))

    employee = Employee(employee_id, name, salary)
    company.add_employee(employee)

company.display_employees()