import os
from pathlib import Path
from loguru import logger

data_folder = Path("../data/raw")
processed_folder = Path("../data/processed")
all_folders = [folder for folder in data_folder.iterdir() if folder.is_dir()]

file_lists = {}
for folder in all_folders:
    logger.info(f"Listing files in {folder}...")
    folder_files = []
    for path in folder.rglob("*"):
        if path.is_file():
            folder_files.append(str(path).replace("\\", "/"))
    file_lists[folder.name] = folder_files

for team, files in file_lists.items():
    file_path = os.path.join(processed_folder, f"{team}_files.txt")
    with open(file_path, "w") as f:
        f.write("\n".join(files))
    logger.info(f"Saved file list for {team} in {file_path}")

print("All file lists have been saved.")