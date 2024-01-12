from To_do_app.Day17.functions import get_todos, write_todos
import time

now = time.strftime('%h %d %Y  %H:%M')
print(f'Today is {now}')


while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todos = get_todos()
        todo = user_action[4:]

        todos.append(todo + '\n')

        write_todos(todos)

    if user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            index = index + 1
            item = item.strip('\n')
            print(f"{index}-{item}")

    if user_action.startswith('edit'):
        try:
            todos = get_todos()

            edit = int(user_action[5:])
            todo_edit = input("Enter edited to-do: ")

            todos[edit - 1] = todo_edit + '\n'

            write_todos(todos)
            print(f"Todo  was replaced by {todo_edit}")

        except ValueError:
            print("Enter correct value")
        except IndexError:
            print("Enter correct Index")

        if user_action.startswith('complete'):
            todos = get_todos()

            complete_todo = int(user_action[9:])

            todos.pop(complete_todo - 1)

            write_todos(todos)
            print(f'Todo {complete_todo} was removed from the list')
    if user_action.startswith('exit'):
        break
print("See YA Mate")
