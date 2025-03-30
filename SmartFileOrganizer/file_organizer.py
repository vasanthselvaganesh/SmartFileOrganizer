import os
import shutil
import csv

# Define categories based on file extensions
CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".ppt", ".csv"],
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Others": []
}

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_files(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            filename, extension, size, filepath = row
            category = get_category(extension)

            # Create folder if not exists
            folder_path = os.path.join(os.path.expanduser("~/Desktop/Organized_Files"), category)
            os.makedirs(folder_path, exist_ok=True)

            # Move the file
            try:
                shutil.move(filepath, os.path.join(folder_path, filename))
                print(f"✅ Moved {filename} -> {folder_path}/")
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")

if __name__ == "__main__":
    organize_files("output.csv")
    print("✅ All files organized successfully!")
