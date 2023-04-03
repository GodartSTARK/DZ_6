import transliterate 
import os
import pathlib
import shutil


def normalize(filename):
    name = str(filename)
    name = transliterate.translit(name, 'ru', reversed=True)
    name = ''.join([char if char.isalnum() or char == '.' or char.isdigit() else '_' for char in name])
    return name


def move(file_path):
    file_extension = os.path.splitext(file_path)[-1].lower()[1:]
    for folder_name, allowed_extensions in dict_folders.items():
        if file_extension in allowed_extensions:
            folder_path = pathlib.Path(folder_name)
            folder_path.mkdir(exist_ok=True)
            new_file_path = folder_path / normalize(file_path.name)
            shutil.move(str(file_path), str(new_file_path))
            #print(f"Moved {file_path} to {new_file_path}")
            return 

dict_folders = {
    'images': ['jpeg', 'png', 'jpg', 'svg'],
    'video': ['avi', 'mp4', 'mov', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'archives': ['zip', 'gz', 'tar'],
    'other': []         
}


source_folder = pathlib.Path(r'd:\testfolder')


for folder_name in dict_folders.keys():
    folder_path = pathlib.Path(folder_name)
    folder_path.mkdir(exist_ok=True)


for file_path in source_folder.glob('**/*'):
    if file_path.is_file():
        move(file_path)