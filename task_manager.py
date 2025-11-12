import time
from logic import TaskList, Task
from rich.console import Console

# Instances
todo = TaskList() 
console = Console()

# Main function call to launch the system or close
def main():
    while True:
        todo.clear_terminal()
        user_input = input(f"Welcome! Would you like to launch the system? \n[1]: Yes\n[2]: No\n")
        if user_input == "1":
            todo.load_tasks()
            main_menu()
        elif user_input == "2":
            break
             
# System launch 
def main_menu():
    while True: 
        todo.clear_terminal()
        print("Main Menu\n")
        print("Current Tasks:\n")
        todo.display_task()
        user_input = input(
            "\nSelect from the list of options:\n" 
            "[1]: Add New Task\n" 
            "[2]: Edit Task\n" 
            "[3]: View Task List\n" 
            "[4]: Remove Task\n"
            "[5]: Clear Tasks\n"
            "[6]: Exit\n")
        if user_input == "1":
            add_task()
        elif user_input == "2":
            edit_task()
        elif user_input == "3":
            view_task()
        elif user_input == "4":
            remove_task()
        elif user_input == "5":
            clear_tasks()
        elif user_input == "6":
            break
            
def add_task():
    while True:
        todo.clear_terminal()
        print("Main Menu > Add New Task\n")
        print("Press 'q' to cancel.\n")
        title_input = input("Enter Task Title: ").strip()
        if todo.existing_task(title_input):
            console.print("[bold red]Warning: Task already exists.[/]")
            time.sleep(1) 
            continue   
        if title_input.lower() == "q":
            return
        title = title_input
        break
    while True:
        days_input = input("Days to complete (e.g., 1, 5, 10): ").strip()       
        if days_input.lower() == "q":
            return
        try:
            if todo.positive_number_check(days_input):  
                raise ValueError
        except ValueError:
            console.print("[bold red]Please enter a valid positive number.[/]")
            time.sleep(1)
            continue
        days = int(days_input)
        break
    new_task = Task(title, days)
    todo.tasks.append(new_task)
    todo.save_tasks()
    todo.clear_terminal()
    console.print(f"[bold green]Task added successfully![/]")
    time.sleep(1.5)   
        

def view_task():
    todo.clear_terminal()
    print("Main Menu > View Task List\n")
    print("Current Tasks:\n")
    todo.display_task()
    while True:
        view_input = input("\nPress 'q' to cancel. ")
        if view_input == "q":
            break

def edit_task():
    todo.clear_terminal()
    print("Main Menu > Edit Task\n")
    print("Current Tasks:\n")
    todo.display_task()
    print("\nPress 'q' to cancel.\n")
    while True:
        try:
            task_number = input("Which task would you like to edit?: ")
            if task_number.lower() == "q":
                return
            task_index = int(task_number) - 1
            if task_index < 0 or task_index >= len(todo.tasks):
                raise ValueError
            break
        except ValueError:
            console.print("[bold red]Please enter task's number rank. (e.g., 1, 2)[/]")
            time.sleep(1)
            continue
    selected_task = todo.tasks[task_index]
    edit_selected_task(selected_task)
    todo.save_tasks()

def edit_selected_task(task):
    while True:
        todo.clear_terminal()
        print("Main Menu > Edit Task List > Edit Selected Task\n")

        # Display selected task to edit
        due_date = task.due_date.strftime("%Y-%m-%d")
        print(f"Selected Task:\n\n\t{task.title} | Due: {due_date}\n")

        edit_task_input = input(
            "What would you like to edit?\n"
            "[1]: Task Title\n"
            "[2]: Days To Complete\n"
            "[3]: ..\n")
        if edit_task_input == "1":
            todo.clear_terminal()
            print("Press 'q' to cancel.\n")
            print(f"Current: {task.title}\n")
            new_title = input("Update Task Title: ").strip()
            if new_title.lower() == "q":
                break
            task.update_title(str(new_title))
            todo.clear_terminal()
            console.print(f"[bold green]Title updated to: {task.title}[/]")
            time.sleep(1.5)
            continue
        elif edit_task_input == "2":
            todo.clear_terminal()
            while True:
                try:
                    print("Press 'q' to cancel.\n")
                    print(f"Current: {due_date}\n")
                    new_days = (input("Update Days To Complete: "))
                    if new_days.lower() == "q":
                        return
                    task.update_days(int(new_days))
                    todo.clear_terminal()
                    console.print(f"[bold green]Days to complete updated to: {task.days_to_complete}[/]")
                    time.sleep(1.5)
                    break
                except ValueError:
                    console.print("[bold red]Invalid Input, Please enter a number.[/]")
                    time.sleep(1)
                    continue
        elif edit_task_input == "3":
            break

def remove_task():
    todo.clear_terminal()
    print("Main Menu > Remove Task\n")
    print("Current Tasks:\n")
    todo.display_task()
    print("\nPress 'q' to cancel.\n")
    while True:
        try:
            task_number = console.input("[bold orange1]Which task would you like to remove?:[/] ")
            if task_number.lower() == "q":
                return
            task_index = int(task_number) - 1
            if task_index < 0 or task_index >= len(todo.tasks):
               raise ValueError
            break
        except ValueError:
            console.print("[bold red]Please enter task's number rank. (e.g., 1, 2)[/]")
            time.sleep(1)
            continue 
    todo.remove_selected_task(task_index)
    todo.save_tasks()
    todo.clear_terminal()
    console.print("[bold green]Your task has been removed![/]")
    time.sleep(1.5)

def clear_tasks():
    todo.clear_terminal()
    print("Main Menu > Clear Tasks\n")
    print("Current Tasks:\n")
    todo.display_task()
    while True:
        try:
            clear_input = console.input("\n[bold orange1]Warning: This action cant be undone (y/n): [/] ")
            if clear_input == "y":
                todo.clear_task_list()
                todo.save_tasks()
                todo.clear_terminal()
                console.print("[bold green]Your tasks have been cleared![/]")
                time.sleep(1.5)
                break
            elif clear_input == "n":
                return
            else: 
                raise ValueError 
        except ValueError:
                console.print("[bold red]Invalid Input: Please enter 'y' or 'n'.")
                time.sleep(1)
                continue

# Function call to begin the program
if __name__ == "__main__":
    main()