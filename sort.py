import os

image_extensions = {".jpg", ".jpeg", ".png", ".gif"}
video_extensions = {".avi", ".mp4", ".mkv", ".mov"}
document_extensions = {".pdf", ".doc", ".docx", ".ppt", ".pptx"}
music_extensions = {".mp3", ".wav", ".flac"}
archive_extensions = {".zip", ".rar", ".tar", ".gz"}

unknown = {}
images = {}
videos = {}
documents = {}
music = {}
archives = {}

# Path to the folder to sort
folder_path = (
    "/path/Users/katerynaturuntseva/Documents/project_test/test_1/home_work_module_6/"
)

# Walk through the directory tree and sort files by extension
for root, dirs, files in os.walk(folder_path):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in image_extensions:
            if "Image" not in images:
                images["Image"] = []
            images["Image"].append(os.path.join(root, file))
        elif ext in video_extensions:
            if "Video" not in videos:
                videos["Video"] = []
            videos["Video"].append(os.path.join(root, file))
        elif ext in document_extensions:
            if "Document" not in documents:
                documents["Document"] = []
            documents["Document"].append(os.path.join(root, file))
        elif ext in music_extensions:
            if "Music" not in music:
                music["Music"] = []
            music["Music"].append(os.path.join(root, file))
        elif ext in archive_extensions:
            if "Archive" not in archives:
                archives["Archive"] = []
            archives["Archive"].append(os.path.join(root, file))
        else:
            if "Unknown" not in unknown:
                unknown["Unknown"] = []
            unknown["Unknown"].append(os.path.join(root, file))

# Create sorted directories and move files to their respective directories
for key, value in images.items():
    new_folder = os.path.join(folder_path, key)
    os.makedirs(new_folder, exist_ok=True)
    for file_path in value:
        new_file_path = os.path.join(new_folder, os.path.basename(file_path))
        os.rename(file_path, new_file_path)

for key, value in videos.items():
    new_folder = os.path.join(folder_path, key)
    os.makedirs(new_folder, exist_ok=True)
    for file_path in value:
        new_file_path = os.path.join(new_folder, os.path.basename(file_path))
        os.rename(file_path, new_file_path)

for key, value in documents.items():
    new_folder = os.path.join(folder_path, key)
    os.makedirs(new_folder, exist_ok=True)
    for file_path in value:
        new_file_path = os.path.join(new_folder, os.path.basename(file_path))
        os.rename(file_path, new_file_path)

for key, value in music.items():
    new_folder = os.path.join(folder_path, key)
    os.makedirs(new_folder, exist_ok=True)
    for file_path in value:
        new_file_path = os.path.join(new_folder, os.path.basename(file_path))
        os.rename(file_path, new_file_path)

for key, value in archives.items():
    new_folder = os.path.join(folder_path, key)
    os.makedirs(new_folder, exist_ok=True)
    for file_path in value:
        new_file_path = os.path.join(new_folder, os.path.basename(file_path))
        os.rename(file_path, new_file_path)

for key, value in unknown.items():
    new_folder = os.path.join(folder_path, key)
    os.makedirs(new_folder, exist_ok=True)
    for file_path in value:
        new_file_path = os.path.join(new_folder, os.path.basename(file_path))
        os.rename(file_path, new_file_path)
