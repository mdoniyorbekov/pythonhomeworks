class Employees:
    def __init__(self, emloyee_id, name, position, salary):
        self.employee_id = emloyee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
class EmployeeManager:
    File_Name = "employees.txt"
    def __init__(self):
        try:
            open(self.File_Name, "a").close
        except:
            print("Error")
    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        with open(self.File_Name, "a") as file:
            file.write(f"{self.employee_id}, {self.name}, {self.position}, {self.salary}\n")
            print ("Emloyee added successfully\n")

    def view_all_employees(self):
        try: 
            with open(self.File_Name, "r") as file:
                employees = file.readlines()
            if not employees:
                print("Emloyee record not found\n")
                return
            print("""Emloyee records:""")
            for empl in employees:
                print(empl.strip())
                print()
        except:
            print("Error\n")

    def search_employee(self):
        search_id = input("Enter Employee id:")
        try:
            with open(self.File_Name, "r") as file:
                employees = file.readlines()
            for empl in employees:
                empl_data = empl.strip().split(', ')
                if empl_data[0] == search_id:
                    print("Employee found")
                    print(empl.strip())
                    return 
            print("Employee not found")
        except:
            print("Error")
    
    def update_employee(self):
        search_id = input("Enter Employee id to update: ")
        try:
            with open(self.File_Name, "r") as file:
                employees = file.readlines()
            updated_employees = []
            found = False
            for empl in employees:
                empl_data = empl.strip().split(', ')
                if empl_data[0] == search_id:
                    print("Current Record:", empl.strip())
                    empl_data[1] = input("Enter a new name: ")
                    empl_data[2] = input("Enter a new position: ")
                    empl_data[3] = input("Enter a new salary: ")
                    found = True
                    print("Employee updated successfully\n")
                updated_employees.append(", ".join(empl_data) + "\n")
                if not found:
                    print("Employee not found\n")
                    return
                with open(self.File_Name, "w") as file:
                    file.writelines(updated_employees)
        except:
            print("Error")
    def menu(self):
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.add_employee()
        elif choice == "2":
            self.view_all_employees()
        elif choice == "3":
            self.search_employee()
        elif choice == "4":
            self.update_employee()
        elif choice == "5":
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()