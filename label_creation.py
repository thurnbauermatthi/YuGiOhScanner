import yaml
from PIL import Image

import shutil

with open("data.yaml", "r") as f:
    data = yaml.full_load(f)

ids = data.get("names")

for i, id in enumerate(ids):
    class_id = i

    base = "raw_data/"

    img = Image.open(base+id+".png")

    size = img.size
    center_x = 0.5
    center_y = 0.5
    width = 1
    height = 1
    label_string = f"{class_id} {center_x} {center_y} {width} {height}"

    shutil.copyfile(base+id+".png", "data/train/images/"+id+".jpg")
    with open("data/train/labels/"+id+".txt", "w") as f:
        f.write(label_string)

