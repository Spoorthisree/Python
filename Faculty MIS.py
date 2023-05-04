import csv

# define file name
filename = "faculty_data.csv"

# define base class for all employees
class Employee:
    def __init__(self, id, name, department,designation,experience):
        self.id = id
        self.name = name
        self.department = department
        self.designation=designation
        self.experience= experience
        
   
    def display(self):
        pass
   
    def calculate_salary(self):
        pass

# define subclass for faculty members
class Faculty(Employee):
    def __init__(self, id, name, department,designation,experience, basic_salary):
        super().__init__(id, name, department,designation,experience)
        self.basic_salary = basic_salary
   
    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Designation:",self.designation)
        print("Experience:",self.experience)
        print("Basic Salary:", self.basic_salary)
    
   
    def calculate_salary(self):
        hra = 0.25 * self.basic_salary
        da = 0.1 * self.basic_salary
        return self.basic_salary + hra + da

# function to add a new faculty member
def add_faculty():
    # get faculty details from user
    id = input("Enter faculty ID: ")
    name = input("Enter faculty name: ")
    department = input("Enter faculty department: ")
    designation=input("Enter the designation: ")
    experience=input("Enter number of years experience: ")
    basic_salary = None
    while basic_salary is None:
        try:
            basic_salary = float(input("Enter faculty basic salary: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    
    # create a faculty object
    faculty = Faculty(id, name, department,designation,experience,basic_salary)
   
    # write faculty details to file
    with open(filename, mode='a', newline='') as faculty_file:
        writer = csv.writer(faculty_file)
        writer.writerow([faculty.id, faculty.name, faculty.department,faculty.designation,faculty.experience,faculty.basic_salary])
   
    print("Faculty details added successfully!")

# function to delete a faculty member
def delete_faculty():
    # get faculty ID from user
    id = input("Enter faculty ID to delete: ")
   
    # read faculty details from file and write all except the one to delete
    rows = []
    found = False
    with open(filename, mode='r') as faculty_file:
        reader = csv.reader(faculty_file)
        for row in reader:
            if row[0] == id:
                found = True
            else:
                rows.append(row)
    if found:
        with open(filename, mode='w', newline='') as faculty_file:
            writer = csv.writer(faculty_file)
            writer.writerows(rows)
        print("Faculty with ID", id, "deleted successfully!")
    else:
        print("Faculty with ID", id, "not found.")

def update_faculty():
    # get faculty ID to update from user
    id = input("Enter faculty ID to update: ")
   
    # read faculty details from file and update the one with the matching ID
    rows = []
    found = False
    with open(filename, mode='r') as faculty_file:
        reader = csv.reader(faculty_file)
        for row in reader:
            if row[0] == id:
                print("Current details:")
                faculty = Faculty(row[0], row[1], row[2],row[3],float(row[4]), float(row[5]))
                faculty.display()
                print("Enter new details:")
                name = input("Enter faculty name: ")
                department = input("Enter faculty department: ")
                designation=input("Enter faculty designation:")
                experience=input("Enter faculty experience:")
                basic_salary = None
                while basic_salary is None:
                    try:
                        basic_salary = float(input("Enter faculty basic salary: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
               
                faculty.name = name
                faculty.department = department
                faculty.designation= designation
                faculty.experience=experience
                faculty.basic_salary = basic_salary
                row = [faculty.id, faculty.name, faculty.department,faculty.designation,faculty.experience,faculty.basic_salary, faculty.calculate_salary()]
                found = True
            rows.append(row)
        if found:
            with open(filename, mode='w', newline='') as faculty_file:
                writer = csv.writer(faculty_file)
                writer.writerows(rows)
            print("Faculty with ID", id, "updated successfully!")
        else:
            print("Faculty with ID", id, "not found.")

# function to search for a faculty member by ID

def search_faculty():
    # get faculty ID to search for from user
    id = input("Enter faculty ID to search for: ")
   
    # search for faculty with the matching ID
    found = False
    with open(filename, mode='r') as faculty_file:
        reader = csv.reader(faculty_file)
        for row in reader:
            if row[0] == id:
                faculty = Faculty(row[0], row[1], row[2],row[3],float(row[4]), float(row[5]))
                faculty.display()
                found = True
                break
   
    if not found:
        print("Faculty with ID", id, "not found.")


#function to display all faculty members
def display_faculty():
    # read faculty details from file and display all
    with open(filename, mode='r') as faculty_file:
       reader = csv.reader(faculty_file)
       for row in reader:
           faculty = Faculty(row[0], row[1], row[2],row[3],float(row[4]), float(row[5]))
           faculty.display()
           print("Total Salary:", faculty.calculate_salary())
           print()


def sort_faculty():
    # get user input for sorting criteria
    print("Sort faculty members by:")
    print("1.Department")
    print("2.Designation")
    print("3.Experience")
    print("4.Salary")
    choice = input("Enter your choice (1/2/3/4): ")
   
    # read faculty details from file and sort based on criteria
    with open(filename, mode='r') as faculty_file:
        reader = csv.reader(faculty_file)
        
        if choice == "1":
            sorted_rows = sorted(reader, key=lambda row: row[2])
            print("Sorted by Department")
        elif choice == "2":
            sorted_rows = sorted(reader, key=lambda row: row[3])
            print("Sorted by Designation")
        elif choice == "3":
            sorted_rows = sorted(reader, key=lambda row: float(row[4]))
            print("Sorted by experience:")
        elif choice == "4":
            sorted_rows = sorted(reader, key=lambda row: float(row[5]))
            print("Sorted by salary:")
        else:
            print("Invalid choice.")
            return
       
        # display sorted faculty members
        for row in sorted_rows:
            faculty = Faculty(row[0], row[1], row[2],row[3],float(row[4]), float(row[5]))
            faculty.display()
            print("Total Salary:", faculty.calculate_salary())
            print()


#main program loop
while True:
    print("Menu:")
    print("1. Add new faculty")
    print("2. Delete faculty")
    print("3. Update faculty")
    print("4. Search faculty")
    print("5. Display all faculty")
    print("6. Sort faculty")
    print("7. Quit")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_faculty()
    elif choice == "2":
        delete_faculty()
    elif choice == "3":
        update_faculty()
    elif choice == "4":
        search_faculty()
    elif choice == "5":
        display_faculty()
    elif choice == "6":
        sort_faculty()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
