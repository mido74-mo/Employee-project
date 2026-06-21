class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age  
        self.salary = salary
    def __str__(self):
        return f"Employee: {self.name} has age {self.age} and salary {self.salary}"


class EmployeeManager:
    def __init__(self):
        self.employee = []

    def add_employee(self, employee):
        self.employee.append(employee)
    
    def list_employee(self):
        if len(self.employee) == 0:
            print("No employees at the moment.")
            return
        print("**Employees list**")
        for emp in self.employee:
            print(emp)

    def remove_employee(self, age_from, age_to):
        for i in range(len(self.employee) - 1, -1, -1):
            emp = self.employee[i]
            if age_from <= emp.age <= age_to:
                print(f"Deleting {emp.name}")
                self.employee.pop(i)

    def update_employee(self, name, new_salary):
        for emp in self.employee:
            if emp.name == name:
                emp.salary = new_salary
                return True
        return False


class Frontend_manager:
    def __init__(self):
        self.manager = EmployeeManager()

    def add_employee(self):
        name = input("enter employee name:")
        age = int(input("enter employee age:"))
        salary = int(input("enter employee salary:"))
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee) 

    def list_employee(self):
        self.manager.list_employee()
        
    def remove_employee(self):
        age_from = int(input("enter lower bound of employee age to remove:"))
        age_to = int(input("enter upper bound of employee age to remove:"))
        self.manager.remove_employee(age_from, age_to)

    def update_employee(self):
        name = input("enter employee name to update salary:")
        new_salary = int(input("enter new salary:"))
        found = self.manager.update_employee(name, new_salary)
        if not found:
           print("Error: No employee with such a name")


if __name__ == "__main__":
    frontend = Frontend_manager()
    while True:
        print("Program Options:")
        print("1) Add a new employee")
        print("2) List all employees")
        print("3) Delete by age range")
        print("4) Update salary given a name")
        print("5) End the program")

        # Input validation loop
        while True:
            choice = input("Enter your choice (from 1 to 5): ")
            try:
                choice_int = int(choice)
                if 1 <= choice_int <= 5:
                    break
                else:
                    print("Invalid range. Try again!")
            except ValueError:
                print("Invalid input. Try again!")

        if choice_int == 1:
            frontend.add_employee()
        elif choice_int == 2:
            frontend.list_employee()
        elif choice_int == 3:
            frontend.remove_employee()
        elif choice_int == 4:
            frontend.update_employee()
        elif choice_int == 5:
            break