import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', size=[45, 10], enable_events=True)
layout = [[label], [input_box, add_button], [list_box, edit_button]]
window = sg.Window("My to-do app", layout, font=('Helvetica', 20))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add':
        todos = functions.get_todos()
        new_todo = values['todo'] + '\n'
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todos'].Widget.yview_moveto(1)  # Scroll to the bottom
    elif event == 'Edit':
        selected_todo_index = values['todos'][0] if values['todos'] else None
        if selected_todo_index is not None:
            new_todo = values['todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(selected_todo_index)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todos'].Widget.yview_moveto(1)  # Scroll to the bottom
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0] if values['todos'] else '')

window.close()
