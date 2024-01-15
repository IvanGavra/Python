import PySimpleGUI as sg
from backend import extract_archive

sg.theme("Black")
input1 = sg.Input()
input2 = sg.Input()
lable1 = sg.Text("Select archive:")
lable2 = sg.Text("Select det dir: ")
button1 = sg.FileBrowse("Choose", key='archive', file_types=(("ZIP Files", "*.zip"),))
button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color="green")

layout = [[lable1, input1, button1], [lable2, input2, button2], [extract_button, output_label]]
window = sg.Window("Archive extractor", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Extract":
        archivepath = values['archive']
        dest_dir = values['folder']
        extract_archive(archivepath, dest_dir)
        window['output'].update(value="Extraction comleted")

window.close()
