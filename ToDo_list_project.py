import os
class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = [line.strip() for line in file]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

    def mark_completed(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task marked as completed!")
            self.save_tasks()
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted!")
            self.save_tasks()
        else:
            print("Invalid task index.")
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            num = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(num)
        elif choice == "4":
            todo_list.view_tasks()
            num = int(input("Enter task number to delete: "))
            todo_list.delete_task(num)
        elif choice == "5":
            print("program over")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
