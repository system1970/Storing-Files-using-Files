# src/file_utils.py
import os
import math
import shutil

def delete_all_files_and_folders(directory_path):
    """
    Deletes all files and subdirectories inside the given directory.
    """
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def create_folder(folder_name):
    """
    Creates a folder if it doesn't exist, or clears it if it does.
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        delete_all_files_and_folders(folder_name)
        print(f"Folder '{folder_name}' cleared and reused.")

def get_file_size(file_path):
    """
    Returns the size of a file in a human-readable format (B, KB, MB, etc.).
    """
    size_bytes = os.path.getsize(file_path)
    return convert_size(size_bytes)

def get_folder_size(folder_path):
    """
    Returns the total size of all files in a folder in a human-readable format (B, KB, MB, etc.).
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return convert_size(total_size)

def convert_size(size_bytes):
    """
    Converts a size in bytes to a human-readable string (B, KB, MB, etc.).
    """
    if size_bytes == 0:
        return "0B"
    
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return f"{s} {size_name[i]}"