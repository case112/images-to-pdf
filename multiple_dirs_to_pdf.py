from PIL import Image
import PySimpleGUI as sg
import os

start_path = os.path.expanduser("~/Desktop")
extension = ()
ext = ''
file_problem = False
problematic_files = []

extensions = (
    '.tif',
    '.tiff',
    '.png',
    '.jpg',
    '.jpeg'
)

checkboxes = [sg.Checkbox(extensions[i], key=extensions[i]) for i in range(len(extensions))]
layout = [
    [
        sg.Text('Select file extension to convert:', pad=((0, 0),(5,2)))
    ],
    checkboxes,
    [
        sg.Text('Convert multiple folders or a single folder:', pad=((0, 0),(20,2)))
    ],
    [
        sg.Radio('Multiple', "RADIO", key='multi', default=True),
        sg.Radio('Single', "RADIO", key='single'),
    ],
    [
        sg.Input(key='user_input_path', enable_events=True, visible=False)
    ],
    [
        sg.FolderBrowse('Browse', enable_events=True, target='user_input_path', size=(10,2), initial_folder=start_path, pad=((0, 0),(20,25))),
        sg.Text('Path:', size=(4,3)), sg.Text(size=(50,3), key='selected_path')
    ],
    [
        sg.Button('Convert', key='convert_btn', disabled=True, button_color=('white', '#2ea44f')),
        sg.Text(' '),
        sg.Button('Exit the program', button_color=('white', '#d73a49'))
    ]      
]

     
def convert_multiple_dirs(selected_directory):
    subfolders = [ f.path for f in os.scandir(selected_directory) if f.is_dir() ]
    if subfolders != []:
        converted_dirs = []
        for subfolder in subfolders:
            selected_directory = subfolder
            converted_dir = convert_dir(selected_directory)
            if converted_dir != None:
                converted_dirs.append(converted_dir)

        print(converted_dirs)
        if converted_dirs != []:
            sg.Popup('Converted ' + str(len(converted_dirs)) + ' folders to location: ' + os.path.normpath(selected_directory + os.sep + os.pardir), title='Done!')
        else:
            sg.Popup('No additional folders with required extensions found! Did you select the right path?', title='Error!')
    else:
        sg.Popup('No additional folders with required extensions found! Did you select the right path?', title='Error!')


def convert_dir(selected_directory):
    global pages
    global file_problem
    global problematic_files
    pages = []
    for file_in_dir in os.listdir(selected_directory):
        if file_in_dir.lower().endswith(extension):
            file_path = selected_directory + os.sep + file_in_dir
            try:
                page = Image.open(file_path)
                pages.append(page.convert("RGB"))
                page.close()
            except:
                file_problem = True
                problematic_files.append(file_in_dir)
            pdf_path_name = os.path.dirname(selected_directory) + os.sep + os.path.basename(selected_directory) + '.pdf'

    if pages != []:
        print("Generating PDF " + pdf_path_name)
        pages[0].save(pdf_path_name, save_all = True, append_images=pages[1:])
        converted_dir = os.path.basename(selected_directory)
        return converted_dir


window = sg.Window('Convert to PDF', layout)

while True:
    event, values = window.read()

    for i in range(len(extensions)):
        if values[extensions[i]] == True and event == 'convert_btn':
            extension += (extensions[i],)
    
    if event == sg.WINDOW_CLOSED or event == 'Exit the program':
        break

    if event == 'user_input_path':
        window.FindElement('convert_btn').Update(disabled=False)
        selected_directory = values['user_input_path']
        window.Element('Browse').InitialFolder = selected_directory

    if event == 'convert_btn' and values['multi'] == True:
        if extension != ():
            file_problem = False
            convert_multiple_dirs(selected_directory)
        if problematic_files != []:
            sg.PopupScrolled(*problematic_files, size=(60, None), title="These files can't be converted:")
            problematic_files = []
        if extension == ():
            sg.Popup('Please select file extension first!', title='Error!')
        extension = ()
        ext = ''

    if event == 'convert_btn' and values['single'] == True:
        if extension != ():
            file_problem = False
            convert_dir(selected_directory)
            if len(pages) > 1 and problematic_files == []:
                sg.Popup('Converted ' + str(len(pages)) + ' images to location: ' + selected_directory + '.pdf', title='Done!')
            if len(pages) > 1 and problematic_files != []:
                sg.Popup('Converted ' + str(len(pages)) + ' images to location: ' + selected_directory + '.pdf', title='Done!')
                sg.PopupScrolled(*problematic_files, size=(60, None), title="These files can't be converted:")
                problematic_files = []
            if file_problem == False and pages == []:
                for x in range(len(extension)):
                    ext += str(extension[x]) + ' '
                sg.Popup('No " ' + ext +'" files found!', title='Error!')
        else:
            sg.Popup('Please select file extension first!', title='Error!')

        extension = ()
        ext = ''

    window['selected_path'].update(values['user_input_path'])

window.close()
