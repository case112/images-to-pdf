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
