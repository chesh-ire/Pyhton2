class Employee:
    count = 0

    def __init__(self):
        self.name = None
        self.place = None
        self.department = None
        Employee.count += 1
        self.eid = 'EMP' + str(Employee.count)

    def update(self):
        self.name = input("Enter Name: ")
        self.place = input("Enter Place: ")
        self.department = input("Enter Department: ")

    def display(self):
        print(f'Employee ID: {self.eid}, Employee Name: {self.name}, Employee Place: {self.place}, Employee Department: {self.department}')

# Prompt user to enter the total number of employees
n = int(input("Enter the total number of Employees: "))

# Create a list to store employee objects
emp_list = []

# Add employee details
for i in range(n):
    emp = Employee()
    emp.update()
    emp_list.append(emp)

# Display the employee details
print("The Employee Details are:")
for emp in emp_list:
    emp.display()