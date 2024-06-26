import os
import shutil

# Specify the path to the folder where your files are located
source_folder = 'C:\\Users\\Administrator\\Desktop\\New Folder'  # Path to the source folder
destination_folder = 'C:\\Users\\Administrator\\Desktop\\New Folder\\Target Folder'  # Path to the target folder

# Ensure the target folder exists, if not, create it
os.makedirs(destination_folder, exist_ok=True)

# Walk through all files and folders in the source directory
for subdir, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(subdir, file)
        # Move files to the target folder
        try:
            shutil.move(file_path, os.path.join(destination_folder, file))
        except Exception as e:
            print(f'Error moving file {file_path}: {e}')

print(f'All files have been moved to {destination_folder}')
