from PIL import Image
from pathlib import Path
import os

#Pulls from the current directory. Will change this to be more versatile in what directory is being used
# path = Path.cwd()
path = r"Path"
#Creates a list of all files in chosen directory that have the .webp extension
webp_files = [f for f in os.listdir(path) if f.endswith(".webp")]

#Loops through all files in list of files, converts them to jpeg and then deletes the webp version out of the directory
for file in webp_files:
    image = Image.open(path + "\\" + file).convert("RGB")
    try:
        image.save(f"{path}\\{file.strip('.webp')}.jpeg", "jpeg")
    except FileNotFoundError:
        image.save(f"{path}\\{file}.jpeg", "jpeg")
    os.remove(path + "\\" + file)


