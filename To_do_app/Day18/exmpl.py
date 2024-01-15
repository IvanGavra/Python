import PySimpleGUI as sg

# Your external list
external_list = ["Item 1", "Item 2", "Item 3", "Item 4"]

# Define the layout with a Listbox element
layout = [
    [sg.Listbox(values=external_list, size=(20, 5), key='listbox')],
    [sg.Button("Show Selected Item"), sg.Button("Exit")]
]

window = sg.Window("External List Example", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Show Selected Item':
        selected_item_index = values['listbox'][0]  # Get the index of the selected item
        if selected_item_index is not None:
            selected_item = external_list[selected_item_index]
            sg.popup(f"Selected Item: {selected_item}")

window.close()
