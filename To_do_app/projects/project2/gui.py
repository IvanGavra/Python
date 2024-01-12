import PySimpleGUI as sg
from To_do_app.projects.project2.func import converter

top_text = sg.Text("Enter feet    ")
low_text = sg.Text("Enter inches")
cnvrt_button = sg.Button("Convert")
input_box1 = sg.InputText(key='input_box1')
input_box2 = sg.InputText(key='input_box2')
output = sg.Text(key='output')
layout = [[top_text, input_box1], [low_text, input_box2], [cnvrt_button, output]]
window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    # Get the values entered in the input boxes
    feet = values['input_box1']
    inches = values['input_box2']

    # Call the converter function with the values
    result = converter(feet, inches)

    # Update the output text element with the result
    window['output'].update(value=result)

window.close()
