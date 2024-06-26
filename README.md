# File Mover Script

This Python script is designed to move all files from all subfolders into a single target folder.

## Requirements

- Python 3.x
- `shutil` module (included in the Python standard library)
- `os` module (included in the Python standard library)

## Installation

1. Open the command prompt and navigate to the directory containing the script 
2. Run the script : python move_files.py

## Usage

1. Place the `move_files.py` script in the directory where your files are located.
2. Edit the script to specify the correct paths for the source and target folders:

   ```python
   source_folder = 'C:\\Users\\Administrator\\Desktop\\New Folder'  # Path to the source folder
   destination_folder = 'C:\\Users\\Administrator\\Desktop\\New Folder\\Target Folder'  # Path to the target folder
