import os
import random
import yaml

images = os.listdir("data_preprocessed/images")
#labels = os.listdir("data_preprocessed/labels")

with open("data.yaml", "r") as f:
    data = yaml.full_load(f)

ids = data.get("names")

for id in ids:
    train_size = 8

    id_images = [i for i in images if i.split(".")[0].split("_")[0] == id]
    if len(id_images) == 0:
        continue
    random.shuffle(id_images)
    train = id_images[:train_size]
    val = id_images[train_size:]

    for t in train:
        os.rename("data_preprocessed/images/"+t, "data/train/images/"+t)
        os.rename("data_preprocessed/labels/"+t.replace(".jpg", ".txt"), "data/train/labels/"+t.replace(".jpg", ".txt"))

    for v in val:
        os.rename("data_preprocessed/images/" + v, "data/valid/images/" + v)
        os.rename("data_preprocessed/labels/" + v.replace(".jpg", ".txt"),
                  "data/valid/labels/" + v.replace(".jpg", ".txt"))
    a = 1
