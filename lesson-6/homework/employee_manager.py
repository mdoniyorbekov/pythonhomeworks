def add_employee():
    with open("employees.txt", "a") as file:
        empl_id = input("Enter employee ID: ")
        empl_name = input("Enter employee name: ")
        empl_position = input("Enter employee position: ")
        empl_salary = input("Enter employee salary: ")
        file.write(f"{empl_id},{empl_name},{empl_position},{empl_salary}/n")
        print("Emloyee record added successfully")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        if records:
            print ("Employee records: ")
            for record in records: 
                print (record.strip())
            else:
                print("No records found")
    except FileNotFoundError: 
        print("No records found. File Doesn't exist yet")

def search_employee():
    empl_id = input("Enter employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            found = False
            for record in file:
                data = record.strip().split(',')
                if data[0] == empl_id:
                    print (f"Employee found: {record.strip()}") 
                    found = True
                    break
                if not found:
                    print("Employee not found: ")
    except FileNotFoundError:
        print("File Does not exist yet")

def update_employees():
    empl_id = input("Enter employee ID to update")
    try:
        with open("employees.txt", "r") as file: 
           records = file.readlines()

           updated = False
           with open("employees.txt", "r") as file: 
               for record in records:
                   data = record.strip().split(",")
                   if data [0] == empl_id:
                       print(f"Current record:{record.strip()}")
                       empl_name = input("Enter new name: ") or data[1]
                       empl_position = input("Enter new position: ") or data[2]
                       empl_salary = input("Enter new salary: ") or data[3]
                       file.write(f"{empl_id}, {empl_name},{empl_position},{empl_salary}\n")
                       updated = True
                   else:
                       file.write(record)

        if updated:
               print("Employee record updated successfully")
        else: 
               print ("emloyee not found")
    except FileNotFoundError:
        print("File does not exist yet")
               
def delete_employee():
    empl_id = input("Enter employee ID to delete: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            with open("employees.txt", "w") as file:
                deleted = False
                for record in records:
                    data = record.strip().split(",")
                    if data[0] != empl_id:
                        file.write(record)
                    else:
                        deleted = True
        if deleted:
            print("Emloyee record deleted succesfully.")
        else: print("Emloyee not found")
                        
    except FileNotFoundError:
        print("File Does not exist yet")
def main():
    while True:
        print("\nEmloyee record manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an emloyee by Emloyee ID")
        print("4. Update and emloyees' information")
        print("5. Delete an emloyee record")
        print("Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employees()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Pleas, try Again")
if __name__ == "__main__":
    main()