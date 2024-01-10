def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def wright_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Enter add, show, edit,complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):

        todos = get_todos('todos.txt')

        todo = user_action[4:]
        todos.append(todo + '\n')

        wright_todos('todos.txt', todos)


    elif user_action.startswith('show'):

        todos = get_todos('todos.txt')

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f'{index + 1}-{todo}')

    elif user_action.startswith('edit'):
        try:

            todos = get_todos('todos.txt')

            edit = int(user_action[5:])
            edit = edit - 1
            edited = input("Enter changes: ")
            todos[edit] = edited + '\n'

            wright_todos('todos.txt', todos)

        except IndexError:
            print("Your index is out of range")
        except ValueError:
            print("Enter actual value")
    elif user_action.startswith('complete'):
        try:

            todos = get_todos('todos.txt')

            completed = int(user_action[9:])
            completed = completed - 1
            todos.pop(completed)
            todo_to_remove = todos[completed].strip('\n')
            wright_todos('todos.txt', todos)
            message = f'Todo {todo_to_remove} was removed from the list'
        except IndexError:
            print("Your complete index out of range")
        except ValueError:
            print("Wrong value")
    elif 'exit' in user_action:
        break
print("Goodbye")
