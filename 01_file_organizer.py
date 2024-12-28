import os
import shutil

input_path = input('Enter file path: ')

if not os.path.exists(input_path):
    raise ValueError("Path does not Exists")

os.chdir(input_path)

videos = ("mp4", "avi", "mkv", "mov", "wmv", "flv", "webm", "mpeg")
audios = ("mp3", "wav", "aac", "flac", "ogg", "wma", "m4a", "opus")
images = ("jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "heic", "webp")
docs = ("pdf", "doc", "docx", "txt", "rtf", "odt", "xls", "xlsx", "ppt", "pptx","deb")

files = os.listdir()
for file in files:
    file_ext = file.split('.')[-1]
    filepath = os.path.join(os.getcwd(), file)
    
    if file_ext in videos:
        shutil.move(filepath, '/home/shanku/Videos')
        
    elif file_ext in audios:
        shutil.move(filepath, '/home/shanku/Music')
        
    elif file_ext in images:
        shutil.move(filepath, '/home/shanku/Pictures')
        
    elif file_ext in docs:
        if not os.path.exists('/home/shanku/Documents/doc'):
            os.mkdir('/home/shanku/Documents/doc')

        shutil.move(filepath, '/home/shanku/Documents/doc')