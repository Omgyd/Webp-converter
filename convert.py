from PIL import Image
from pathlib import Path
import os

path = Path.cwd()
webp_files = [f for f in os.listdir(path) if f.endswith(".webp")]

for file in webp_files:
    image = Image.open(file).convert("RGB")
    image.save(f"{file.strip('.webp')}.jpeg", "jpeg")
    os.remove(file)


