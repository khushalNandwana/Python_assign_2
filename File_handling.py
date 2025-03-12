def write():
    file= open(r"C:\Users\khush\Documents\kevon projects\Python_assign_2\file_handling\students.txt", "w")
    while True:
            name = input("Enter student name: ")
            if name.lower() == 'done':
                break
            try:
                age = int(input("Enter student age: "))
                marks = float(input("Enter student marks: "))
            except ValueError:
                print("Error = Please insert correct input")
                continue
            ch = input("Y->Yes\nN->No\nEnter your choice")
            if ch == 'n' or ch == 'N':
                break
    file.write(f"Name: {name}, Age: {age}, Marks: {marks}\n")


def read():
    try:
        file=open(r"C:\Users\khush\Documents\kevon projects\Python_assign_2\file_handling\students.txt", "r")
        contents = file.read()
        print("\nStudent Information")
        print(contents)
    except FileNotFoundError:
        print("Error: students.txt not found.")


# Main program execution
write()
print("program run successfully")
read()
print("program over here...")
