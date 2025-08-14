class ToDolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        task = {"task": task_description, "done": False}
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task["task"].lower() == task_name.lower():
                self.tasks.remove(task)
                print("Task removed successfully.")
                return
        print("Task not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
            return

        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")
        print()

    def mark_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDolist()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task by Name")
        print("3. Display Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_desc = input("Enter task description: ")
            todo_list.add_task(task_desc)

        elif choice == '2':
            task_name = input("Enter task name to remove: ")
            todo_list.remove_task(task_name)

        elif choice == '3':
            todo_list.display_tasks()

        elif choice == '4':
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                todo_list.mark_complete(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
