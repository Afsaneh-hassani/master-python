# import modules and global variables

import shutil
from pathlib import Path

base_dir= Path (r"C:\\Users\\lappixel\\Downloads")
target_dir= base_dir/ "sorted"


# definition file categories

FILE_CATEGORIES = {

    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],

    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],

    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],

    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],

    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"]    

}


# creating file directories

def create_file_category():
    for category,_ in FILE_CATEGORIES.items():
        (target_dir/category).mkdir(parents=True,exist_ok=True)
        




# search and categorize file

def search_and_categorize():
    for file in base_dir.rglob("*"):
        
        for category,extentions in FILE_CATEGORIES.items():
            if file.suffix in extentions:
                try:
                    shutil.copy(file,target_dir / category)
                except shutil.SameFileError:
                    pass
                    
            




create_file_category()
search_and_categorize()
