while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter todo :") + "\n"
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item}'
                print(row)
        case 'edit':
            number = input(("Enter todo to edit: "))
            number = int(number) - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            edited = input("edit todo: ")
            todos[number] = edited
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            compleated_todo = int(input("Enter completed todo number: "))
            index = compleated_todo - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todos_to_remove} is removed from your list'
            print(message)
        case 'exit':
             break
print("Goodbye")

