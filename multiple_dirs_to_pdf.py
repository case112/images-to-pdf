from PIL import Image
import PySimpleGUI as sg
import os
import time

start_path = os.path.expanduser("~/Desktop")
extension = ()
ext = ''
file_problem = False

extensions = (
    '.tif',
    '.tiff',
    '.png',
    '.jpg',
    '.jpeg'
)

layout = [
    [
        sg.Text('Select file extension to convert:')
    ],
    [
        sg.Checkbox(extensions[0], key=extensions[0], default=True),
        sg.Checkbox(extensions[1], key=extensions[1]),
        sg.Checkbox(extensions[2], key=extensions[2]),
        sg.Checkbox(extensions[3], key=extensions[3]),
        sg.Checkbox(extensions[4], key=extensions[4]),
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

#os.chdir("/path/to/change/to")
     
def convert():
    global pages
    global file_problem
    pages = []
    subfolders = [ f.path for f in os.scandir(selected_directory) if f.is_dir() ]

    if subfolders != []:

        for subfolder in subfolders:

            for file_in_dir in os.listdir(subfolder):
                if file_in_dir.lower().endswith(extension):
                    file_path = subfolder + os.sep + file_in_dir
                    try:
                        page = Image.open(file_path)
                        pages.append(page.convert("RGB"))
                        page.close()
                    except:
                        pages = []
                        file_problem = True
                        return sg.Popup('There is a problem with "' + file_in_dir + '", it is not possible to convert this file. Aborting. Fix this and please try again.', title='Warning!')  

                    pdf_path_name = os.path.dirname(subfolder) + os.sep + os.path.basename(subfolder) + '.pdf'

            if pages != []:
                print("Generating PDF " + pdf_path_name)
                pages[0].save(pdf_path_name, save_all = True, append_images=pages[1:])
                pages = []

    else:
        print('no folders found')

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
    
    if event == sg.WINDOW_CLOSED or event == 'Exit the program':
        break

    if event == 'user_input_path':
        window.FindElement('convert_btn').Update(disabled=False)
        selected_directory = values['user_input_path']
        window.Element('Browse').InitialFolder = selected_directory

    if event == 'convert_btn':
        if extension != ():
            file_problem = False
            convert()
            if len(pages) > 1:
                sg.Popup('Converted ' + str(len(pages)) + ' images to location: ' + selected_directory, title='Done!')
            #if file_problem == False and pages == []:
                #for x in range(len(extension)):
                    #ext += str(extension[x]) + ' '
                #sg.Popup('No " ' + ext +'" files found!', title='Error!')
        else:
            sg.Popup('Please select file extension first!', title='Error!')

        extension = ()
        ext = ''

    window['selected_path'].update(values['user_input_path'])

window.close()
