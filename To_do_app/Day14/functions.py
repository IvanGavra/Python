def get_todos(filepath='todos.txt'):
    """Read the file and return list of to-do in todos"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """Write, edit and poping items from todos.txt file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print("Hello from functions")
