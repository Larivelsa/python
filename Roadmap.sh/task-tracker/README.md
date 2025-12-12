# Task Tracker

A simple command-line based Task Tracker application written in Python.

## Overview

Task Tracker is a small CLI tool to help you manage daily tasks — add, list, update, and remove tasks — saving all tasks in a JSON file so that your data persists between runs.

## Features

- Add new tasks  
- List all existing tasks  
- Update a task by its ID  
- Delete a task by its ID  
- Persist tasks in a JSON file on disk  

## Requirements

- Python 3.7 or newer  
- No external dependencies (only built-in Python modules — e.g. `json`, `argparse` or `sys`)  

## Usage

Run from the command line:

```bash
# Add a new task
python task_tracker.py add "Buy groceries"

# List all tasks
python task_tracker.py list

# Update a task (ID 1 in this example)
python task_tracker.py update 1 "Buy fruits and veggies"

# Delete a task (ID 1)
python task_tracker.py delete 1

Font: https://roadmap.sh/projects/task-tracker

