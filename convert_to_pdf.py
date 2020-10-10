from PIL import Image
import glob
import tkinter as tk
import os


extensions = [
    '.tif',
    '*.tiff',
    '*.jpg',
    '*.jpeg'
]

extension = extensions[0]

selected_directory = os.getcwd() + os.sep

print(selected_directory)



def convert():
    pages = []
    for file_in_dir in os.listdir(selected_directory):
        if file_in_dir.endswith(extension):
            file_path = selected_directory + file_in_dir
            page = Image.open(file_path)
            print(page)
            print(file_path)
            pages.append(page.convert("RGB"))
    print("Generating PDF")
    pages[0].save("out.pdf", save_all = True, append_images=pages[1:])


convert()