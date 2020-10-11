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
    [sg.FolderBrowse('Select folder to convert', key='user_input_path'),
    sg.Text('Path:'), sg.Text(size=(50,3), key='selected_path')],
    [sg.Button('Convert', disabled=True), sg.Button('Exit the program')]
          
]

          
window = sg.Window('Convert to PDF', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    print(event, values)


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

    #if event == 'Select folder to convert':
        #window['selected_path'].update(values['user_input_path'])
    # Output a message to the window
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