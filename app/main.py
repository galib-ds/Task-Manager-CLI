from app.tasks import (
    add_task, 
    get_tasks,
    complete_task,
    delete_task,
)

def main() -> None:

    while True:
        print(f"=== Task Manager ===")
        print(f"1. Add task\n2. View tasks\n3. Complete task\n4. Delete task\n5. Exit")
        
        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Please enter a number (1, 2 or 3): ")
            continue

        if choice == 1:   
            title = input("Enter a task: ")
            try:
                task = add_task(title)
                print(f"Created task #{task['id']}: {task['title']}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == 2:
            
            get_tasks()

        elif choice == 3:
            
            try:
                task_id = int(input("Enter task ID to complete: "))

                task = complete_task(task_id)

                print(f"Completed task #{task["id"]: {task["title"]}}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == 4:
            
            try:
                task_id = int(input("Enter task ID to delete: "))

                task = delete_task(task_id)

                print(f"Deleted task #{task['id']}: {task['title']}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == 5:
            
            print("Bye bye...")
            break

        else:
            print("Invalid choice.\nPlease choose 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    main()