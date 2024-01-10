#from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todos = functions.get_todos()

        todo = user_action[4:]
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            index = index + 1
            item = item.strip('\n')
            row = (f'{index}-{item}')
            print(row)
    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            edit = int(user_action[4:])
            item_for_editing = input("Enter what you want to edit: ")
            todos[edit - 1] = item_for_editing + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Wrong value")
    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            index_completed = int(user_action[9:])
            todos.pop(index_completed - 1)
            functions.write_todos(todos)
        except IndexError:
            print("Your index is wrong")
    elif user_action.startswith('exit'):
        break
print("Bye Mate")
