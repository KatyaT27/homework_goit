import os
import sys
import shutil

# Define file extensions for different file types
image_extensions = {".jpg", ".jpeg", ".png", ".gif"}
video_extensions = {".avi", ".mp4", ".mkv", ".mov"}
document_extensions = {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".txt", ".xlsx"}
music_extensions = {".mp3", ".wav", ".flac"}
archive_extensions = {".zip", ".rar", ".tar", ".gz"}
unknown_extensions = {}

# Function to normalize file and folder names
def normalize(name): # ця функція замінює крапку в назві файлу, треба переробити
    """
    Replace spaces with underscores and remove other non-alphanumeric characters.
    """
    return "".join(c if c.isalnum() else "_" for c in name.replace(" ", "_"))

# Path to the folder to sort
folder_path = sys.argv[1]

# Walk through the directory tree and sort files by extension
for root, dirs, files in os.walk(folder_path):
    # Exclude certain directories from processing
    # print(root)
    # print(dirs)
    # print(files)
    dirs[:] = [d for d in dirs if d not in ["archives", "video", "audio", "documents", "images"]]
    # якщо використовуєте list comprehension то це має бути в одному рядку
    for file in files:
        # Get the file extension
        ext = os.path.splitext(file)[1].lower()
        # print("ext= ", ext)
        # Check the file type and move it to the appropriate directory
        if ext in image_extensions:
            if "Image" not in dirs:
                if not os.path.exists(os.path.join(folder_path, "Image")): # потрібно робити перевірку чи існує така папка. Така перевірка потрібна для кожної службової папки
                    os.mkdir(os.path.join(folder_path, "Image")) # потрібно вказувати саме folder_path, тому що root на кожній наступный ітерації змінюеться на глубину папки.
            dest_dir = os.path.join(folder_path, "Image")
        elif ext in video_extensions:
            if "Video" not in dirs:
                os.mkdir(os.path.join(folder_path, "Video"))
            dest_dir = os.path.join(folder_path, "Video")
        elif ext in document_extensions:
            if "Document" not in dirs:
                if not os.path.exists(os.path.join(folder_path, "Document")):
                    os.mkdir(os.path.join(folder_path, "Document"))
            dest_dir = os.path.join(folder_path, "Document")
        elif ext in music_extensions:
            if "Music" not in dirs:
                os.mkdir(os.path.join(folder_path, "Music"))
            dest_dir = os.path.join(folder_path, "Music")
        elif ext in archive_extensions:
            # Extract the archive to a subdirectory of the "archives" directory
            archive_path = os.path.join(folder_path, file)
            archive_name = os.path.splitext(file)[0]
            extract_path = os.path.join(folder_path, "archives", normalize(archive_name))
            print('extract_path', extract_path)
            if not os.path.exists(extract_path):
                os.mkdir(os.path.join(folder_path, "archives")) # потрібно спочатку творити папку archives
                os.mkdir(extract_path)
            shutil.unpack_archive(archive_path, extract_path)
            # continue
        else:
            # Move files with unknown extensions to a directory named "Unknown"
            # if "Unknown" not in dirs:
            if not os.path.exists(os.path.join(folder_path, "Unknown")):
                os.mkdir(os.path.join(folder_path, "Unknown"))
            dest_dir = os.path.join(folder_path, "Unknown")
        # Move the file to the appropriate directory
        src_path = os.path.join(root, file)
        print('src_path ', src_path)
        dest_path = os.path.join(dest_dir, file)
        print('dest_path', dest_path)
        os.rename(src_path, dest_path)

# Delete empty directories
for root, dirs, files in os.walk(folder_path, topdown=False):
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        if not os.listdir(dir_path):
            os.rmdir(dir_path)
