from PIL import Image
import PySimpleGUI as sg
import os
import time

start_path = os.path.expanduser("~/Desktop")

extensions = (
    '.tif',
    '.tiff',
    '.dng',
    '.png',
    '.jpg',
    '.jpeg'
)
extension = ()
ext = ''

layout = [
    [
        sg.Text('Select image extension to convert:')
    ],
    [
        sg.Checkbox(extensions[0], key=extensions[0]),
        sg.Checkbox(extensions[1], key=extensions[1]),
        sg.Checkbox(extensions[2], key=extensions[2]),
        sg.Checkbox(extensions[3], key=extensions[3]),
        sg.Checkbox(extensions[4], key=extensions[4]),
        sg.Checkbox(extensions[5], key=extensions[5]),
    ],
    [
        sg.Text(' ')
    ],
    [
        sg.Input(key='user_input_path', enable_events=True, visible=False)
    ],
    [
        sg.FolderBrowse('Browse', enable_events=True, target='user_input_path', size=(10,2), initial_folder=start_path),
        sg.Text('Path:', size=(4,3)), sg.Text(size=(50,3), key='selected_path')
    ],
    [
        sg.Text(' ')
    ],
    [
        sg.Button('Convert', key='convert_btn', disabled=True, button_color=('white', '#2ea44f')),
        sg.Text(' '),
        sg.Button('Exit the program', button_color=('white', '#d73a49'))
    ]      
]

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

window = sg.Window('Convert to PDF', layout)

while True:
    event, values = window.read()

    if values[extensions[0]] == True and event == 'convert_btn':
       extension += (extensions[0],)
    if values[extensions[1]] == True and event == 'convert_btn':
       extension += (extensions[1],)
    if values[extensions[2]] == True and event == 'convert_btn':
       extension += (extensions[2],)
    if values[extensions[3]] == True and event == 'convert_btn':
       extension += (extensions[3],)
    if values[extensions[4]] == True and event == 'convert_btn':
       extension += (extensions[4],)
    if values[extensions[5]] == True and event == 'convert_btn':
       extension += (extensions[5],)
    
    if event == sg.WINDOW_CLOSED or event == 'Exit the program':
        break

    if event == 'user_input_path':
        window.FindElement('convert_btn').Update(disabled=False)
        selected_directory = values['user_input_path']
        window.Element('Browse').InitialFolder = selected_directory
        pdf_path_name = os.path.dirname(selected_directory) + os.sep + os.path.basename(selected_directory) + '.pdf'

    if event == 'convert_btn':
        if extension != ():
            convert()
            if len(pages) > 1:
                sg.Popup('Converted ' + str(len(pages)) + ' images to location: ' + pdf_path_name, title='Done!')
            else:
                for x in range(len(extension)):
                    ext += str(extension[x]) + ' '
                sg.Popup('No " ' + ext +'" files found!', title='Error!')
        else:
            sg.Popup('Please select file extension first!', title='Error!')

        extension = ()
        ext = ''

    window['selected_path'].update(values['user_input_path'])

window.close()

