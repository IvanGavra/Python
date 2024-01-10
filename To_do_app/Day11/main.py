def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add,show, edit, continue or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if 'show' in user_action:

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip()
            index = index + 1
            print(f'{index}-{item}')

    elif 'edit' in user_action:
        try:
            user_input = int(user_action[5:])
            new_todo = input("Enter new todo :")

            todos = get_todos()

            todos[user_input - 1] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except IndexError:
            print("Enter a correct index to edit")
            continue
        except ValueError:
            print("Enter a correct value to edit")
            continue


    else:
        if 'complete' in user_action:
            try:
                completed = int(user_action[9:])
                completed = completed - 1

                todos = get_todos()

                todos.pop(completed)

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
            except IndexError:
                print(f"No index for complete, try index in range form 1 to {len(todos)} or type show")
