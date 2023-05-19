import os
import shutil
import re

# Визначення розширень файлів для різних типів файлів
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".svg"}
video_extensions = {".avi", ".mp4", ".mkv", ".mov"}
document_extensions = {".pdf", ".doc",
                       ".docx", ".ppt", ".pptx", ".txt", ".xlsx"}
music_extensions = {".mp3", ".wav", ".flac"}
archive_extensions = {".zip", ".rar", ".tar", ".gz"}
unknown_extensions = {}


def normalize(string):
    # Транслітерувати кириличні символи на латинські
    char_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie',
        'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
        'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu',
        'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E',
        'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ь': '',
        'Ю': 'Yu', 'Я': 'Ya'
    }
    for cyrillic_char, latin_char in char_map.items():
        string = string.replace(cyrillic_char, latin_char)
    # Замінити символи, що не є літерами або цифрами, на підкреслення
    string = re.sub(r'[^a-zA-Z0-9]', '_', string)
    return string

# Функція для сортування файлів за типами і переміщення їх в відповідні каталоги


def sort_files(folder_path):
    dest_dir = None  # Ініціалізую dest_dir значенням None
    for root, dirs, files in os.walk(folder_path):
        # Виключаємо певні каталоги
        dirs[:] = list(filter(lambda d: d not in {
                       "archives", "video", "audio", "documents", "images"}, dirs))
        for file in files:
            # Отримуємо розширення файлу
            ext = os.path.splitext(file)[1].lower()
            # Перевіряємо тип файлу і переміщуємо його в відповідний каталог
            if ext in archive_extensions:
                archive_dir_path = os.path.join(folder_path, "archives")
                if not os.path.exists(archive_dir_path):
                    os.mkdir(archive_dir_path)
                # Розпаковуємо архів в підкаталог каталогу "archives"
                archive_path = os.path.join(root, file)
                archive_name = os.path.splitext(file)[0]
                extract_path = os.path.join(
                    archive_dir_path, normalize(archive_name))
                if not os.path.exists(extract_path):
                    os.mkdir(extract_path)
                shutil.unpack_archive(archive_path, extract_path)
            elif ext in image_extensions:
                images_dir_path = os.path.join(folder_path, "images")
                if not os.path.exists(images_dir_path):
                    os.mkdir(images_dir_path)
                dest_dir = images_dir_path
            elif ext in video_extensions:
                video_dir_path = os.path.join(folder_path, "video")
                if not os.path.exists(video_dir_path):
                    os.mkdir(video_dir_path)
                dest_dir = video_dir_path
            elif ext in document_extensions:
                documents_dir_path = os.path.join(folder_path, "documents")
                if not os.path.exists(documents_dir_path):
                    os.mkdir(documents_dir_path)
                dest_dir = documents_dir_path
            elif ext in music_extensions:
                audio_dir_path = os.path.join(folder_path, "audio")
                if not os.path.exists(audio_dir_path):
                    os.mkdir(audio_dir_path)
                dest_dir = audio_dir_path
            else:
                if ext not in unknown_extensions:
                    unknown_extensions[ext] = 0
                unknown_extensions[ext] += 1
                continue

            # Перевіряємо, чи була задоволена будь-яка з умов
            if dest_dir is not None:
                # Переміщуємо файл у відповідний каталог
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.move(src_file_path, dest_file_path)
                print(f"Переміщено файл: {file} у {dest_dir}")

                # Рекурсивно викликаємо функцію для підкаталогів
                sort_files(dest_dir)

    # Видаляємо порожні каталоги
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


# Шлях до каталогу для сортування
folder_path = input("Введіть шлях до каталогу для сортування: ")

# Сортуємо файли
sort_files(folder_path)

def main():
    # Шлях до каталогу для сортування
    folder_path = sys.argv[1]

    # Сортуємо файли
    sort_files(folder_path)


if __name__ == '__main__':
    main()
тоді 
entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
