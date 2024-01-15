import functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal1")

clock = sg.Text("", key='clock')
lable = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      size=[45, 10], enable_events=True)
layout = [[clock],
          [lable],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [ exit_button]]
window = sg.Window("My to-do app", layout, font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%H:%M %D'))
    print(event)
    print(values)
    #print(values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case sg.WIN_CLOSED:
            break

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Select an Item first", font=('Helvatica', 20))
        case 'Complete':
            try:
                completed_todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(completed_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Select item for complete")
        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'])



window.close()
