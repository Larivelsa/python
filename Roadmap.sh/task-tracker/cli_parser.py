import argparse

def create_parser():
    parser = argparse.ArgumentParser(prog='task-cli')

    subparsers = parser.add_subparsers(
        dest='command',
        required=True
    )

    # task-cli add 'Buy milk'
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('description')

    # task-cli update 1 'Buy bread'
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('id', type=int)
    update_parser.add_argument('description')

    # task-cli delete 1
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('id', type=int)

    # task-cli mark-in-progress 1
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress')
    mark_in_progress_parser.add_argument('id', type=int)

    # task-cli mark-done 1
    mark_done_parser = subparsers.add_parser('mark-done')
    mark_done_parser.add_argument('id', type=int)

    # task-cli list
    # task-cli list todo
    # task-cli list done
    # task-cli list in-progress
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument(
        'status',
        nargs='?',
        choices=['todo', 'in-progress', 'done']
    )

    return parser