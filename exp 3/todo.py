import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Added task: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[✓]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['task']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Marked task {index} as done.")
    else:
        print("Invalid task number.")

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed['task']}")
    else:
        print("Invalid task number.")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple CLI To-Do List")
    parser.add_argument("command", choices=["add", "list", "done", "remove"], help="Action to perform")
    parser.add_argument("--task", help="Task description (for add)")
    parser.add_argument("--index", type=int, help="Task index (for done/remove)")
    args = parser.parse_args()

    if args.command == "add" and args.task:
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done" and args.index:
        mark_done(args.index)
    elif args.command == "remove" and args.index:
        remove_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
