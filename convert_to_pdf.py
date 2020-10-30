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
    first_page = False
    pages = []
    counter = -1
    pdf_path_name = os.path.dirname(selected_directory) + os.sep + os.path.basename(selected_directory) + '.pdf'
    print(sorted(os.listdir(selected_directory)))
    for file_in_dir in sorted(os.listdir(selected_directory)):
        counter += 1

        if file_in_dir.lower().endswith(extension):
            file_path = selected_directory + os.sep + file_in_dir
            print(file_path)
            try:
                page = Image.open(file_path)
                page = (page.convert("RGB"))
                pages.append(file_path)
                if first_page == False:
                    page.save(pdf_path_name, append_images=page)
                    first_page = True
                else:
                    page.save(pdf_path_name, append=page)
                page.close()

            except:
                file_problem = True
                problematic_files.append(file_in_dir)


        if not sg.one_line_progress_meter(
            'Converting...',
            counter+1,
            len(os.listdir(selected_directory)),
            'key',
            'Currently converting: ' + os.path.basename(selected_directory),
            no_titlebar=True,
            grab_anywhere=True):
            break
            

    if pages != []:
        print("Generated PDF " + pdf_path_name)
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
