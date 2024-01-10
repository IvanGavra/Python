todos = []

while True:
    user_acation = input("Type add, show or exit: ")
    user_acation = user_acation.strip()
    match user_acation:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        #case bullshit:
            #print("Bullshit - try again!")
print("bye!")
