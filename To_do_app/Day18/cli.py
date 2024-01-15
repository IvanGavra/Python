from To_do_app.Day18.functions import get_todos, write_todos
import time

now = time.strftime('%H:%M %d-%m %Y')
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
            item = item.strip('\n')
            print(f'{index}-{item}')

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            index_edit = int(user_action[5:])
            new_todo = input("Enter todo to edit: ") + '\n'
            edited_todo = todos[index_edit - 1]
            todos[index_edit - 1] = new_todo

            write_todos(todos)
            print(f"{edited_todo.strip} was replaced by {new_todo}")
        except ValueError:
            print("Incorrect value")
        except IndexError:
            print("Incorrect index")

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()
            complete_todo = int(user_action[9:])

            todos.pop(complete_todo)
            write_todos(todos)
        except IndexError:
            print("Incorrect index")
    elif user_action.startswith('exit'):
        break
print("See Ya Mate")




