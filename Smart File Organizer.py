# ========== Smart File Manager ==========
print("========== Welcome to Ali's Smart File Manager ==========")
import os
import shutil 

folder_path = r"D:\04_Backups\02 Drive\[01] ALI"
image_folder = os.path.join(folder_path, "Images")
video_folder = os.path.join(folder_path, "Videos")
pdf_folder = os.path.join(folder_path, "PDFs")
txt_folder = os.path.join(folder_path, "Text Files")
others_folder = os.path.join(folder_path, "Others")

os.makedirs(image_folder, exist_ok = True)
os.makedirs(video_folder, exist_ok = True)
os.makedirs(pdf_folder, exist_ok = True)
os.makedirs(others_folder, exist_ok = True)
os.makedirs(txt_folder, exist_ok = True)

files = os.listdir(folder_path)

for file in files:
    full_path = os.path.join(folder_path, file)
    if os.path.isfile(full_path):
        if file.lower().endswith(".pdf"):
            shutil.move(full_path, pdf_folder)
            print(f"File Moved to PDFs: {file}")
        elif file.lower().endswith(".jpg") or file.lower().endswith(".png"):
            shutil.move(full_path, image_folder)
            print(f"File Moved to Images: {file}")
        elif file.lower().endswith(".mp4"):
            shutil.move(full_path, video_folder)
            print(f"File Moved to Videos: {file}")
        elif file.lower().endswith(".txt"):
            shutil.move(full_path, txt_folder)
            print(f"File Moved to Text Files: {file}")
        else:
            shutil.move(full_path, others_folder)
            print(f"File Moved to Others: {file}")