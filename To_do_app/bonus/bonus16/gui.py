import PySimpleGUI as sg
import zip_creator


lable1 = sg.Text("Select file to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

lable2 = sg.Text("Select estination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")
output_lable = sg.Text(key="output")
window = sg.Window("Compressor",
                   layout=[[lable1, input1, choose_button1],
                           [lable2, input2, choose_button2],
                           [compress_button, output_lable]])

while True:
    event, values = window.read()
    print(event, values)
    filepath =values["files"].split(";")
    folder = values["folder"]
    zip_creator.make_archive(filepath, folder)
    window["output"].update(value="Compression completed")
window.close()
