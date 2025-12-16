from models import Task 
from config import DATA_FILE, current_date
import json
import os

def create_json_file():
   if not os.path.exists(DATA_FILE):
      try:
         with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(list(), file)
      except OSError:
         print('Error: Unable to create data file.')

def load_tasks():   
   create_json_file() 
   try:
      with open(DATA_FILE, 'r', encoding='utf-8') as file:
         return json.load(file) 
   except json.JSONDecodeError as e:
      print('Warning: Task data could not be loaded. An empty list will be used.')
      return []
   
json_list = load_tasks()

def generate_id():
   if not json_list:
      return 1
   else:
      return json_list[-1]['id'] + 1

def save_task(tasks):
   try:
      with open(DATA_FILE, 'w', encoding='utf-8') as file:
         json.dump(tasks, file, indent=4)
   except OSError:
      print('Error: Unable to save task to disk.')

def add_task(description):
   t1 = Task(
      id=generate_id(),
      description=description,
      status='todo',
      created_at=current_date,
      updated_at=None
   )

   json_list.append(t1.__dict__)
   save_task(json_list)

   print(f"Task added successfully! ID: {t1.id}")


def update_task(id, description):
    if not json_list:
        print("No tasks to update.")
        return

    for item in json_list:
        if item['id'] == id:
            item['description'] = description
            item['updated_at'] = current_date
            save_task(json_list)
            print(f"Task {id} updated successfully.")
            return

    print(f"Task {id} not found.")

         
def delete_task(id):
    if not json_list:
        print("No tasks to delete.")
        return

    for item in json_list:
        if item['id'] == id:
            json_list.remove(item)
            save_task(json_list)
            print(f"Task {id} deleted successfully.")
            return

    print(f"Task with ID {id} not found.")


def mark_in_progress_or_done(id, status):
   if not json_list:
      print("No tasks to update.")
      return

   for item in json_list:
      if item['id'] == id:
         item['status'] = status
         item['updated_at'] = current_date
         save_task(json_list)
         print(f"Task {id} updated successfully.")
         return

   print(f"Task with ID {id} not found.")


def list_tasks(status=None):
   if not json_list:
      print("No tasks found.")
      return
   
   for item in json_list:
         if status is not None and item['status']!= status:
            continue
            
         print(
            f'[ID {item["id"]}] {item["description"]}\n'
            f'{"Status":12}: {item["status"]}\n'
            f'{"Created at":12}: {item["created_at"]}\n'
            f'{"Updated at":12}: {item["updated_at"]}\n'
            f'{"-" * 40}'
         )


