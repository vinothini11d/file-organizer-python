import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.java', '.c', '.cpp', '.js', '.html', '.css', '.php'],
}

# Function to get file category
def get_category(file_extension):
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

# Function to organize files
def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"❌ Directory does not exist: {directory}")
        return

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Skip if it's a folder
        if os.path.isdir(item_path):
            continue

        # Extract file extension and determine category
        _, extension = os.path.splitext(item)
        category = get_category(extension)

        # Create category folder if it doesn't exist
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)

        # Handle duplicates (rename if file already exists)
        destination = os.path.join(category_folder, item)
        base, ext = os.path.splitext(item)
        counter = 1
        while os.path.exists(destination):
            destination = os.path.join(category_folder, f"{base}_{counter}{ext}")
            counter += 1

        # Move file into the category folder
        shutil.move(item_path, destination)
        print(f"✅ Moved: {item} → {category}/")

    print("\n🎉 File organization complete.")

# Main entry point
if __name__ == "__main__":
    target_dir = r"D:\MS CS NOTES"   # 👈 Your folder path
    organize_files(target_dir)
