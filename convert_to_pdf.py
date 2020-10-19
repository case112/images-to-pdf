from PIL import Image
import PySimpleGUI as sg
import os

start_path = os.path.expanduser("~/Desktop")
extension = ()
ext = ''
file_problem = False
problematic_files = []
ICON = b'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'

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
        sg.Radio('Multi', "RADIO", key='multi', default=True),
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


window = sg.Window('Convert Images to PDF', layout, icon=ICON)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Exit the program':
        break

    for i in range(len(extensions)):
        if values[extensions[i]] == True and event == 'convert_btn':
            extension += (extensions[i],)

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
