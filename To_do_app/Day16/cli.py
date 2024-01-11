from To_do_app.Day16.functions import get_todos, write_todos
import time



now = time.strftime('%H:%M %A %D')
print(now)
while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todos = get_todos()
        todo = user_action[4:]
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            index = index + 1
            item = item.strip("\n")
            print(f'{index}-{item}')

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            item_to_edit = int(user_action[5:])
            todos[item_to_edit - 1] = (input("Enter value for edit: ") + '\n')

            write_todos(todos)
        except ValueError:
            print("Enter value to edit")
        except IndexError:
            print("Enter correct number")

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            complete = int(user_action[9:])
            todos.pop(complete - 1)

            write_todos(todos)
            print(f'{complete} was removed from the todos')
        except ValueError:
            print("Enter correct value to complete")
        except IndexError:
            print("Enter correct number to complete")

    elif user_action.startswith('exit'):
        break
print("See YA Fella")
