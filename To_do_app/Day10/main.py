
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('todos.txt', 'r') as file:
            content = file.readlines()

        for index, item in enumerate(content):
            item = item.strip()
            row = f'{index + 1}-{item}'
            print(row)


    elif user_action.startswith('edit'):
        try:
            index_to_edit = int(user_action[5:])
            edited_item = input("enter value: ")

            with open('todos.txt', 'r') as file:
                editor = file.readlines()
            editor[index_to_edit - 1] = edited_item + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(editor)
        except ValueError:
            print("Yor command is not Valid")
            continue


    elif user_action.startswith('complete'):
        try:
            index_for_complete = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                completed = file.readlines()
            completed.pop(index_for_complete - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(completed)
        except IndexError:
            print("You out of the list of todo, last index is " + str((len(completed))))
            continue
    else:
        if user_action.startswith('exit'):
            break
print("Thank you, and goodbye")
