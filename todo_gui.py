import tkinter as tk
from tkinter import messagebox
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

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["done"] = True
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        del tasks[index]
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

# Load existing tasks
tasks = load_tasks()

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add", command=add_task)
add_button.pack(side=tk.RIGHT)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

mark_done_button = tk.Button(root, text="Mark as Done", command=mark_done)
mark_done_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove", command=remove_task)
remove_button.pack(pady=5)

update_listbox()

root.mainloop()