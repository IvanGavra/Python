import PySimpleGUI as sg
from back import converter
import os

sg.theme("Black")
title = sg.Text("Converter")
input_feet = sg.Input(key='feet')
input_inches = sg.Input(key='inches')
title_feet = sg.Text("Enter feet    ")
title_inches = sg.Text("Enter inches")
output = sg.Text('', key='output')
convert_button = sg.Button("Convert", size=20)
exit_buttnoy = sg.Button("Exit")
layout = [[title],[title_feet, input_feet],[title_inches, input_inches], [convert_button, exit_buttnoy, output]]
window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    try:
        match event:
            case "Convert":

                feet = values['feet']
                inches = values['inches']
                result = converter(feet, inches)
                window['output'].update(value=result)
            case "Exit":
                break
    except ValueError:
        sg.Popup("Enter two numbers")
window.close()
