from PIL import Image
import glob
import tkinter as tk
import os
import PySimpleGUI as sg

extensions = [
    '.tif',
    '.tiff',
    '.png',
    '.jpg',
    '.jpeg'
]


layout = [
    [sg.Text('Select image extension to convert:')],
    [
        sg.Radio(extensions[0], "RADIO", key=extensions[0], default=True),
        sg.Radio(extensions[1], "RADIO", key=extensions[1]),
        sg.Radio(extensions[2], "RADIO", key=extensions[2]),
        sg.Radio(extensions[3], "RADIO", key=extensions[3]),
        sg.Radio(extensions[4], "RADIO", key=extensions[4]),
    ],
    [sg.Text(' ')],
    [sg.Input(key='user_input_path', enable_events=True, visible=False)],
    [sg.FolderBrowse('Select folder to convert', enable_events=True, target='user_input_path', size=(10,2)),
    sg.Text('Path:', size=(4,3)), sg.Text(size=(50,3), key='selected_path')],
    [sg.Text(' ')],
    [
        sg.Button('Convert', key='convert_btn', disabled=True, button_color=('white', '#2ea44f')),
        sg.Text(' '),
        sg.Button('Exit the program', button_color=('white', '#d73a49'))]
          
]

          
window = sg.Window('Convert to PDF', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    print(event, values)
    random = 4

    if values[extensions[0]] == True and event == 'Convert':
       sg.Popup("button 1 pressed")
    elif values[extensions[1]] == True and event == 'Convert':
       sg.Popup("button 2 pressed")
    elif values[extensions[2]] == True and event == 'Convert':
       sg.Popup("button 3 pressed")
    elif values[extensions[3]] == True and event == 'Convert':
       sg.Popup("button 4 pressed")
    elif values[extensions[4]] == True:# and event == 'Convert':
       sg.Popup("button 5 pressed")
       print('something')
       print(values['user_input_path'])
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit the program':
        break

    if event == 'user_input_path':
        window.FindElement('convert_btn').Update(disabled=False)


    window['selected_path'].update(values['user_input_path'])

# Finish up by removing from the screen
window.close()




extension = extensions[0]
selected_directory = os.getcwd()
pdf_path_name = os.path.dirname(selected_directory) + os.sep + os.path.basename(selected_directory) + '.pdf'

def convert():
    pages = []
    for file_in_dir in os.listdir(selected_directory):
        if file_in_dir.lower().endswith(extension):
            file_path = selected_directory + os.sep + file_in_dir
            page = Image.open(file_path)
            pages.append(page.convert("RGB"))
    if pages != []:
        print("Generating PDF")
        pages[0].save(pdf_path_name, save_all = True, append_images=pages[1:])
    else:
        print('No files found')

#convert()