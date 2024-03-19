import Download_cleaning
import os
import shutil

if __name__ == "__main__":
    user_name = input("Input your user name:")
    OneDrive = ""
    while True:
        OneDrive = input("Do you use One Drive (Yes or No):").lower()
        if OneDrive == "yes":
            OneDrive = True
            break
        elif OneDrive == "no":
            OneDrive = False
            break
        else: print("please say yes or no")

    download_path = "C:/Users/" + user_name + "/Downloads"

if os.path.isdir(download_path):
    Download_cleaning.clean_folder(download_path,user_name,OneDrive)
    print("Done Cleaning")
else:
    print("Path do downloads is invalid. Please ensure the download_path is the correct path")