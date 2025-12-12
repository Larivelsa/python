from models import Task 
from datetime import datetime
import json
import os

# add

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_json_file():
   if not os.path.exists('data.json'):
      with open('data.json', 'w', encoding='utf-8') as file:
         json.dump(list(), file)

def load_tasks():   
   create_json_file() 
   with open('data.json', 'r', encoding='utf-8') as file:
      data = json.load(file) 
   return data
   
json_list = load_tasks()

def generate_id():
   if len(json_list) == 0:
      return 1
   else:
      return json_list[len(json_list)-1].get('id')+1

def save_task(tasks):
   with open('data.json', 'w', encoding='utf-8') as file:
      json.dump(tasks, file, indent=4)

def add_task(list_command):   
   t1 = Task(          
          id=generate_id(), 
          description=list_command[1].strip('"'), 
          status="todo", 
          created_at=current_date, 
          updated_at=None)
   
   json_data = t1.__dict__
   json_list.append(json_data)
   save_task(json_list)
   print(f"Task added successfully! ID: {t1.id}")

# update

def update_task(list_command):
   id_searched = int(list_command[1])
   task_update = list_command[2].strip('"')

   for item in json_list:
      if item.get('id') == id_searched:
            item['description']=task_update
            item['updated_at']=current_date
         
   save_task(json_list)

def delete_task(list_command):
   id_searched = int(list_command[1])

   for item in json_list:
      if item.get('id') == id_searched:
         print(item)
         json_list.remove(item)

   save_task(json_list)

def mark_in_progress_or_done(list_command):
   in_progress_or_done = list_command[0]
   id_searched = int(list_command[1])   
   print(in_progress_or_done)

   for item in json_list:
      if item.get('id') == id_searched:
         item['status']=in_progress_or_done[5:]
         item['updated_at']=current_date

   save_task(json_list)


def list_all():
   for item in json_list:
      id = item.get('id') 
      description = item.get('description') 
      status = item.get('status') 
      created_at = item.get('created_at') 
      updated_at = item.get('updated_at') 

      print(f'ID: {id} | Decription: {description} | Status: {status} | Created at: {created_at} | Updated at: {updated_at}')

def list_by_status(status_list):
   for item in json_list:
      id = item.get('id') 
      description = item.get('description') 
      status = item.get('status') 
      created_at = item.get('created_at') 
      updated_at = item.get('updated_at') 
      
      if status == status_list: 
         print(f'ID: {id} | Decription: {description} | Status: {status} | Created at: {created_at} | Updated at: {updated_at}')

