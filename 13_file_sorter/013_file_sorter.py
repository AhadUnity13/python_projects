import os
import shutil

#Define a function create_folder that takes a folder path and an extension.
#Extract the folder name (excluding the dot) from the extension.
#Create a new folder if it doesn't exist using os.makedirs.
#Return the folder path.

def create_folder(path: str, extension: str) -> str:
    folder_name = extension[1:]  
    folder_path = os.path.join(path, folder_name)  
    if not os.path.exists(folder_path):  
        os.makedirs(folder_path)  
    return folder_path  

#Define a function sort_files to walk through the source path recursively (os.walk).
#For each file, get its extension, call create_folder to get the target folder.
#Move the file into the respective folder using shutil.move.

def sort_files(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path = os.path.join(root_dir, filename)
            extension = os.path.splitext(filename)[1] 
            if extension:  
                target_folder = create_folder(source_path, extension)
                target_path = os.path.join(target_folder, filename)
                shutil.move(file_path, target_path) 


#Define a function remove_empty_folders that walks through the folders in a bottom-up order (topdown=False).
#For each folder, check if it's empty and remove it if it is using os.rmdir

def remove_empty_folders(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path = os.path.join(root_dir, current_dir)
            if not os.listdir(folder_path):  
                os.rmdir(folder_path)  


#The main() function should get user input for the folder path.
#Check if the path exists using os.path.exists().
#Call sort_files and remove_empty_folders if the path is valid, else print an error message.

def main():
    user_input = input('Please provide a file path to sort: ')  
    if os.path.exists(user_input):  
        sort_files(user_input)
        remove_empty_folders(user_input)
        print('Files sorted successfully!')
    else:
        print('Invalid path, please provide a valid file path.')  


if __name__ == '__main__':
    main()
