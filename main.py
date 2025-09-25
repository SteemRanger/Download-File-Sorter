import os

f_path = "C:/Users/lukma/Downloads" #original folder from where the file are extracted

files = os.listdir(f_path)

path = "C:/Users/lukma/Desktop/Chest_sorter"
#file paths where files are moved
document_loc = path + "/Documents"
aplication_loc = path + "/Executables"
image_loc = path + "/Images"
video_loc = path + "/Videos"
music_loc = path + "/Music"
conf_loc = path + "/Configurations"
archive_loc = path + "/Archives"
other_loc = path + "/___other___"

def FileRename(fileName):
    i = 1
    fixedFileName = fileName
    while os.path.exists(document_loc + "/" + fileName) == True:
        fileName = fixedFileName[:fixedFileName.find(".")] + "(" + str(i) + ")" + fixedFileName[fixedFileName.find("."):]
        i+=1
    return fileName

for n in files: #recogises files end and moves them
    if n.find(".pdf") != -1 or n.find(".docx") != -1 or n.find(".txt") != -1:
        if os.path.exists(document_loc + "/" + n) == True:
            pathFunction = document_loc + "/" + n
            os.rename(f_path + "/" + n,document_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,document_loc + "/" + n)

    elif n.find(".exe") != -1 or n.find(".msi") != -1:
        if os.path.exists(aplication_loc + "/" + n) == True:
            pathFunction = aplication_loc + "/" + n
            os.rename(f_path + "/" + n,aplication_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,aplication_loc + "/" + n)

    elif n.find(".jpg") != -1 or n.find(".png") != -1 or n.find(".jpeg") != -1 or n.find(".gif") != -1:
        if os.path.exists(image_loc + "/" + n) == True:
            pathFunction = image_loc + "/" + n
            os.rename(f_path + "/" + n,image_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,image_loc + "/" + n)

    elif n.find(".mp4") != -1 or n.find(".mov") != -1 or n.find(".avi") != -1:
        if os.path.exists(video_loc + "/" + n) == True:
            pathFunction = video_loc + "/" + n
            os.rename(f_path + "/" + n,video_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,video_loc + "/" + n)

    elif n.find(".mp3") != -1 or n.find(".wav") != -1:
        if os.path.exists(music_loc + "/" + n) == True:
            pathFunction = music_loc + "/" + n
            os.rename(f_path + "/" + n,music_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,music_loc + "/" + n)

    elif n.find(".conf") != -1 or n.find(".ini") != -1:
        if os.path.exists(conf_loc + "/" + n) == True:
            pathFunction = conf_loc + "/" + n
            os.rename(f_path + "/" + n,conf_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,conf_loc + "/" + n)
        
    elif n.find(".zip") != -1 or n.find(".rar") != -1 or n.find(".7z"):
        if os.path.exists(archive_loc + "/" + n) == True:
            pathFunction = archive_loc + "/" + n
            os.rename(f_path + "/" + n,archive_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,archive_loc + "/" + n)

    else:
        if os.path.exists(other_loc + "/" + n) == True:
            pathFunction = other_loc + "/" + n
            os.rename(f_path + "/" + n,other_loc + "/" + FileRename(n))
            
        else:
            os.replace(f_path + "/" + n,other_loc + "/" + n)
        