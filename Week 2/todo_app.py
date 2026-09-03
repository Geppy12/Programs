#!/usr/bin/env python3
"""
Simple To-Do List Application
"""

def display_menu():
    print("\n=== To-Do List ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("================\n")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✓ Task added: {task}")
    else:
        print("Task cannot be empty!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")

def remove_task(tasks):
    if not tasks:
        print("\nNo tasks to remove!")
        return
    
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"✓ Removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
