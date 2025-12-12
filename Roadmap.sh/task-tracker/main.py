from crud import add_task, update_task, delete_task, mark_in_progress_or_done, list_all, list_by_status

while True:
    command = input("Type the command:")

    list_command_exit = command.split(maxsplit=1)
    list_command_list = command.split(maxsplit=1)
    list_command_add = command.split(maxsplit=1)
    list_command_update = command.split(maxsplit=2)
    list_command_delete = command.split(maxsplit=1)
    list_command_mark_in_progress_or_done = command.split(maxsplit=1)
    
    if list_command_add[0] == "add":
        add_task(list_command_add)

    elif list_command_update[0] == "update":        
        update_task(list_command_update)

    elif list_command_delete[0] == "delete":
        delete_task(list_command_delete)

    elif list_command_mark_in_progress_or_done[0] in ('mark-in-progress', 'mark-done'):
        mark_in_progress_or_done(list_command_mark_in_progress_or_done)

    elif list_command_list[0] == 'list' and len(list_command_list)==1:
        list_all()

    elif list_command_list[0] == 'list' and list_command_list[1] in ('done','in-progress', 'todo'):
        list_by_status(list_command_list[1])

    elif list_command_exit[0] == "exit":
        print("Exiting the program.")
        break
    else:
        print('Please type a correct command.')