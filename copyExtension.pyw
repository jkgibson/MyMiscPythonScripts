#! python3
# copyFileExt.py - Copies all files in a folder containing
# file extension input by user

import sys, shutil, os

# Get the file extension we want to search for. These will be passed
# in via the command line.
extension = sys.argv[1]

# Get the folder we want to search in.
folder = sys.argv[2]


# TODO: Define the function that will do the actual work. It's inputs will be
#       folder and extension

def copyFileExt(folder, extension):
    # Get the absolute path to the inputted folder
    folder = os.path.abspath(folder)
    new_folder = folder + '_' + extension + 's_backup'
    os.makedirs(new_folder)
    # Walk through the folder and it's subfolders, looking for filenames
    # ending in the extension input by the user.
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                print('Copying file %s to new folder' % (filename))
                path=os.path.join(foldername,filename)
                shutil.copy(path, new_folder)
          
            
copyFileExt(folder, extension)   

