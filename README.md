File Splitter
File Splitter is a Python script that takes a large group of files and automatically divides them up into smaller chunks in subfolders. The script is designed to make   it easy to organize a large number of files, especially image files, in a way that makes them easy to navigate and manage.

Features
Organizes files with a specified extension in the source folder and moves them to subfolders in the destination folder.
By default, the script organizes .JPG files in chunks of 25 files per subfolder.
The source and destination folder can be easily configured to the desired location.
The script creates subfolders with the name format "folder{folder_count}" in the destination folder.

How to use
Download the script and place it in the directory where you want to organize your files.
Open the script and modify the source_folder variable to the location of the files you want to organize.
Modify the destination_folder variable to the location where you want to create the subfolders.
Modify the file extension in the script as well to organize other file types.
Run the script by executing python file_organizer.py in the command line.

Requirements
Python 3.x
os module

Note
Please make sure that you have the necessary permissions to read, write and execute the script in the folder where you want to organize your files.
 
Additional Notes
The script will move the files from the source folder to the destination folder and subfolders, so make sure to backup any important files before running the script.
The script will overwrite any existing subfolders in the destination folder with the same name format "folder{folder_count}".
The script will not move any files that do not have the specified extension.
If you have a large number of files, the script may take some time to organize them all.

Conclusion
File Organizer is a simple and easy to use script that can help you organize a large number of files in a structured and manageable way. Whether you have a collection of images, documents, or other types of files, the script can help you keep them organized and easy to find.
