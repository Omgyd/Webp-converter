import os
from PIL import Image

path = r"C:\Users\Lowry\Downloads"

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".webp"):
            file_name = os.path.join(root, name)
            image = Image.open(file_name).convert("RGB")
            try:
                image.save(f"{file_name.strip('.webp')}.jpeg", "jpeg")
            except:
                print("Failed")
            os.remove(file_name)







