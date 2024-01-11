todos = []

while True:
    user_cation = input("Type add, show, edit or exit:")
    user_cation = user_cation.strip()

    match user_cation:
        case 'add':
            todo = input(("Enter to do: "))
            todos.append(todo)
        case 'show':
            print(todos)
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
print("Bye")
