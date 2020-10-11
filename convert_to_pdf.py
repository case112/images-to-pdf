from PIL import Image
import PySimpleGUI as sg
import os

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
    [
        sg.FolderBrowse('Select folder to convert', enable_events=True, target='user_input_path', size=(10,2)),
        sg.Text('Path:', size=(4,3)), sg.Text(size=(50,3), key='selected_path')
    ],
    [sg.Text(' ')],
    [
        sg.Button('Convert', key='convert_btn', disabled=True, button_color=('white', '#2ea44f')),
        sg.Text(' '),
        sg.Button('Exit the program', button_color=('white', '#d73a49'))]      
]
     
window = sg.Window('Convert to PDF', layout)


def convert():
    global pages
    pages = []
    for file_in_dir in os.listdir(selected_directory):
        if file_in_dir.lower().endswith(extension):
            file_path = selected_directory + os.sep + file_in_dir
            page = Image.open(file_path)
            pages.append(page.convert("RGB"))
    if pages != []:
        print("Generating PDF")
        pages[0].save(pdf_path_name, save_all = True, append_images=pages[1:])


while True:
    event, values = window.read()

    if values[extensions[0]] == True and event == 'convert_btn':
       extension = extensions[0]
    elif values[extensions[1]] == True and event == 'convert_btn':
       extension = extensions[1]
    elif values[extensions[2]] == True and event == 'convert_btn':
       extension = extensions[2]
    elif values[extensions[3]] == True and event == 'convert_btn':
       extension = extensions[3]
    elif values[extensions[4]] == True and event == 'convert_btn':
       extension = extensions[4]
    
    if event == sg.WINDOW_CLOSED or event == 'Exit the program':
        break

    if event == 'user_input_path':
        window.FindElement('convert_btn').Update(disabled=False)
        selected_directory = values['user_input_path']
        pdf_path_name = os.path.dirname(selected_directory) + os.sep + os.path.basename(selected_directory) + '.pdf'

    if event == 'convert_btn':
        convert()
        if len(pages) > 1:
            sg.Popup('Converted ' + str(len(pages)) + ' images to location: ' + pdf_path_name)
        else:
            sg.Popup('No "' + extension +'" files found!')

    window['selected_path'].update(values['user_input_path'])

window.close()

