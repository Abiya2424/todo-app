tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        tasks.append(input("Task: "))
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        num = int(input("Number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
    elif choice == "4":
        break
