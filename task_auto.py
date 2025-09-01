import os
import shutil

source_folder = r"C:\Users\piyus\OneDrive\Desktop\Folder 1"
destination_folder = r"C:\Users\piyus\OneDrive\Desktop\Folder 2"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file_name in os.listdir(source_folder):
    print("Found file:", file_name)  # show detected files
    if file_name.lower().endswith((".jpg", ".jpeg")):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        print(f"Moving {source_path} → {destination_path}")  # show movement
        shutil.move(source_path, destination_path)

print("✅ Done. Check Folder 2 now!")
