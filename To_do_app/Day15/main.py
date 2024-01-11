from To_do_app.Day15.functions import read_todos, write_todos
import time

now = time.strftime('%h-%d - %Y %H:%M:%S')
print("It is " + now)

while True:
    user_cation = input(("Enter add, show, edit, complete or exit: "))
    user_cation = user_cation.strip()

    if user_cation.startswith('add'):
        todos = read_todos()

        todo = user_cation[4:]
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_cation.startswith('show'):
        todos = read_todos()
        for index, item in enumerate(todos):
            index = index + 1
            item = item.strip('\n')
            print(f'{index}-{item}')

    elif user_cation.startswith('edit'):
        try:
            todos = read_todos()
            edit = int(user_cation[5:])
            editing = input("Enter item to edit: ")
            todos[edit - 1] = editing + '\n'

            write_todos(todos)
        except ValueError:
            print("Enter todo number to edit: ")

    elif user_cation.startswith('complete'):
        try:
            todos = read_todos()
            complete = int(user_cation[9:])
            todos.pop(complete - 1)

            write_todos(todos)
        except IndexError:
            print("You enter wrong index, try again: ")

    elif user_cation.startswith('exit'):
        break
print("bye-bye")
