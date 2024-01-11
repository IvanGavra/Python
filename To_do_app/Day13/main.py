#todos = []
def read_todos(filepath='todos.txt'):
    """read a file and return todos list items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """write items todos list and text file"""
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

while True:
    user_action = input("enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todos = read_todos()

        todo = user_action[4:]
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = read_todos()

        for index, item in enumerate(todos):
            index = index + 1
            item = item.strip('\n')
            print(f'{index}-{item}')
    elif user_action.startswith('edit'):
        try:
            todos = read_todos()
            edit = int(user_action[5:])
            user_edit = input("Enter item to edit: ")
            todos[edit - 1] = user_edit + '\n'
            write_todos(todos)
        except IndexError:
            print("Wrong index, try again")
        except ValueError:
            print("Wrong value, try agian")
    elif user_action.startswith('complete'):
        try:
            completed = int(user_action[9:])
            todos.pop(completed - 1)
            write_todos(todos)
        except IndexError:
            print("Wrong item number, try again")
    elif user_action.startswith('exit'):
        break
print("See Ya mate")
