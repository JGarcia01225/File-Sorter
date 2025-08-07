import os, shutil
import time
path = r"C:/Users/Drago/Downloads/" #folder it checks for files
file_name = os.listdir(path) #list of files in the folder

folder_names = ['Video files', 'Image files', 'Document files', 'Zip files']  #set of folder names to create
for loop in range(0,4): 
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])

def sort_files():
    for file in file_name:
        if ".mp4" in file and not os.path.exists(path + "Video files/" + file):
            shutil.move(path + file, path + "Video files/" + file)
        elif (".jpg" in file or ".png" in file) and not os.path.exists(path + "Image files/" + file):
            shutil.move(path + file, path + "Image files/" + file)
        if (".txt" in file or ".pdf" in file) and not os.path.exists(path + "Document files/" + file):
            shutil.move(path + file, path + "Document files/" + file)
        elif (".zip" in file or ".rar" in file) and not os.path.exists(path + "Zip files/" + file):
            shutil.move(path + file, path + "Zip files/" + file)
        else:
            print("Unknown file type could not be moved.")
    
while(True):
    sort_files()
    time.sleep(86400) # Once a day
#this code sorts files in a folder into subfolders based on their file type
