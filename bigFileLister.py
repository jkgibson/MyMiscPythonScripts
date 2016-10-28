#! python3
# bigFileLister.py - Search a folder for all files above a value selected
#                 by the user

import shutil, os

# Define a function that takes in folder and specified file size limit,
# and output's to the screen all of the files that exceed this limit.
def bigFileLister(folder, limit):

    # Get the absolute path to the folder
    folder = os.path.abspath(folder)

    # Create a list to contain the names and extensions of the large files.
    big_list = []

    # Walk through the folder and it's subfolders.
    for foldername, subfolder, filenames in os.walk(folder):
        # If a file has size greater then the size limit, put it into the
        # the large file list.
        for filename in filenames:
            path = os.path.join(foldername, filename)
            size = os.path.getsize(path)
            if (size > limit):
                big_list.append(filename)

    # Return the list
    return big_list

# Print the list by calling the function
print(bigFileLister("C:\\test", 1024))
