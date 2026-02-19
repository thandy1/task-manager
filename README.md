# CLI Task Manager

A simple command-line task manager written in Python.  
Allows users to add, edit, view, remove, and clear tasks, with CSV-based persistent storage. Uses [Rich](https://github.com/Textualize/rich) for colored text and better CLI presentation.

---

### Installation

1. **Ensure Python is installed** (Python 3.8 or higher) 
```bash

python --version    # Windows

python3 --version   # Linux/macOS
```

2. **Clone the repository**

```bash
# HTTPS
git clone https://github.com/thandy1/task-manager.git

# SSH
git clone git@github.com:thandy1/task-manager.git
```

3. **Navigate to the program directory**
```bash
cd task-manager
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

### Usage

1. Run the main program:
```bash
python task_manager.py
```

2. Follow the CLI prompts to add, edit, view, remove, or clear tasks.

3. All tasks are automatically saved to `storage.csv` and loaded when the program starts.

---

### Quick Start Example

1. **Add a new task**:
```text
Enter Task Title: Finish Project
Days to complete (e.g., 1, 5, 10): 7
```

2. **View tasks**:
```text
Current Tasks:
    1. Finish Project | Due: 2025-09-01
```

3. **Edit or remove tasks** using the corresponding menu options.

---

### Features

- Add, edit, view, and remove tasks
- Clear all tasks
- Load and save tasks automatically to a CSV file (`storage.csv`)
- CLI interface with Rich for colored font decorations
- Test file included as boilerplate to run your own tests
- Auto-creation and management of CSV storage

---

### Notes

- Fully CLI-based, no GUI.

- The only external library required is Rich for terminal styling.

- Tasks are automatically saved after each change.

---

### Contributing

I’m new to Python and GitHub, so this is a beginner-friendly project.  
If you’d like to contribute, feel free to fork the repository, make changes, and submit a pull request.  
Any feedback or tips are welcome!
