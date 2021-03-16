import os,shutil
import time

folders = {
    'audio':['.mp3','.wav'],
    'video':['.mp4','.mkv'],
    'images':['.jpg','.png','.jpeg'],
    'documents':['.txt','.docx','.csv','.xls','.pdf','.rar']
}

def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder))==True:
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))


def create_move(ext,file_name):
    find=False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            find=True
            break

    if(find!=True):
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,other_name))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))




directory = input('Enter the location:')
other_name = input("Enter folder names for unknown files:")
rename_folder()
all_files = os.listdir(directory)
#print(all_files)
Length = len(all_files)
count = 1
for i in all_files:
    if os.path.isfile(os.path.join(directory,i))==True:
        create_move(i.split(".")[-1],i)
    print(f"Total Files:{Length}| Done:{count}| Left:{Length-count}")
    count+=1
else:
    print("file not found")
time.sleep(2)
a= input("press any key for  Quit")

