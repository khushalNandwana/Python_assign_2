class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def add_details(self):
        my_file = open(r"C:\Users\khush\Documents\kevon projects\Python_assign_2\file_handling\Employee.txt", "a")
        my_file.write(f"{self.name},{self.age},{self.salary}\n")
        print("data saved successfully.\n")

    @staticmethod
    def display_detail():
        try:
            my_file = open(r"C:\Users\khush\Documents\kevon projects\Python_assign_2\file_handling\Employee.txt", "r")
            contents = my_file.read()
            if contents:
                print("\nEmployee Information")
                print(contents)
            else:
                print("NO Information found")
        except FileNotFoundError:
            print("\nError=please enter the correct information")


while True:
    print("\n1. Add the employee data")
    print("2. Display the employee data")
    print("3. Exit")
    choice =input("Enter your choice")
    if choice=='1':
        name = input("Enter the employee's name")
        age = input("Enter the Employee's age")
        salary =input("Enter the Employee's Salary")
        data = Employee(name, age, salary)
        data.add_details()
    elif choice=='2':
        Employee.display_detail()
    elif choice=='3':
        print("Program end here...")
        break
    else:
        print("Invalid input")

