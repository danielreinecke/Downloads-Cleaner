import os
import shutil

def clean_folder(path,user_name,OneDrive):
    for filename in os.listdir(path):
        if OneDrive:
            if os.path.isfile(os.path.join(path, filename)):
                if filename != "desktop.ini":
                    file_type = filename.split(".")[-1].lower()

                    if file_type == "txt" or file_type == "pdf" or file_type == "docx" or file_type == "csv" or file_type == "pptx":
                        shutil.move(os.path.join(path, filename), os.path.join("C:/Users/" + user_name + "/OneDrive/Documents/", filename))
                    elif file_type == "png" or file_type == "jpg" or file_type == "jpeg" or file_type == "avif":
                        shutil.move(os.path.join(path, filename), os.path.join("C:/Users/" + user_name + "/OneDrive/Pictures/", filename))
        else:
            if os.path.isfile(os.path.join(path, filename)):
                if filename != "desktop.ini":
                    file_type = filename.split(".")[-1].lower()

                    if file_type == "txt" or file_type == "pdf" or file_type == "docx" or file_type == "csv" or file_type == "pptx":
                        shutil.move(os.path.join(path, filename), os.path.join("C:/Users/" + user_name + "/Documents/", filename))
                    elif file_type == "png" or file_type == "jpg" or file_type == "jpeg" or file_type == "avif":
                        shutil.move(os.path.join(path, filename), os.path.join("C:/Users/" + user_name + "Pictures/", filename))



