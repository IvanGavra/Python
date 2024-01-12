import To_do_app
from To_do_app.Day17.functions import get_todos, write_todos
import PySimpleGUI as sg

lable = sg.Text("Type in Your to-do")
theme = sg.theme('DarkAmber')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=To_do_app.Day17.functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
input_box = sg.InputText(tooltip="Enter todo", key="todo")

window = sg.Window("My to-do's",
                   layout=[[lable], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
   # print(values['todos'])
    match event:
        case 'Add':
            todos = To_do_app.Day17.functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)

            To_do_app.Day17.functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = To_do_app.Day17.functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            To_do_app.Day17.functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()


