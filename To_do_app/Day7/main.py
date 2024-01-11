while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter todo :") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()


            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item}'
                print(row)
        case 'edit':
            numbers = input("Enter todo to edit: ")
            edited = input("edit todo: ")
            todos[numbers - 1] = edited
        case 'complete':
             compleated_todo = input("Enter completed todo number: ")
             todos.pop(compleated_todo - 1)
        case 'exit':
             break
print("Goodbye")

