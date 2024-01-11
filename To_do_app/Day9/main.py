while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
            todo = user_action[4:]
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
    elif 'show' in user_action:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item}'
                print(row)
    elif 'edit' in user_action:
            number = int(user_action[5:])
            number = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            edited = input("edit todo: ")
            todos[number] = edited + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
    elif 'complete' in user_action:
            index = int(user_action[9:])
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            #compleated_todo = int(input("Enter completed todo number: "))
            index = index - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todos_to_remove} is removed from your list'
            print(message)
    elif 'exit' in user_action:
             break
    else:
        print("Command is not valid")

print("Goodbye")

