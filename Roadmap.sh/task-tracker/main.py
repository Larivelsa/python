from cli_parser import *
from crud import *

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)

    elif args.command == 'update':
        update_task(args.id, args.description)

    elif args.command == 'delete':
        delete_task(args.id)

    elif args.command == 'mark-in-progress':
        mark_in_progress_or_done(args.id, 'in-progress')

    elif args.command == 'mark-done':
        mark_in_progress_or_done(args.id, 'done')

    elif args.command == 'list':
        list_tasks(args.status)

if __name__ == '__main__':
    main()