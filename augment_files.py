import yaml
from PIL import Image, ImageFilter
import os

base = "data_preprocessed/images"
base_label = "data_preprocessed/labels/"
originals = os.listdir(base)
with open("data.yaml", "r") as f:
    data = yaml.full_load(f)

originals = [o for o in originals if "_" not in o]
for file in originals:
    original_image = Image.open(base+"/" + file)
    file_id = file.replace(".jpg", "")
    id = data.get("names").index(file_id)
    label = f"{id} {0.5} {0.5} {1} {1}"

    #rotated_cc_5 = original_image.rotate(5)
    #rotated_cc_5.save(base+ "/" + file_id + "_rotated_cc_5.jpg")
    with open(base_label + file_id + "_rotated_cc_5.txt", "w") as f:
        f.write(label)

    #blured_1_r_cc_5 = rotated_cc_5.filter(ImageFilter.GaussianBlur(1))
    #blured_1_r_cc_5.save(base+ "/" + file_id + "_blur_1_rotated_cc_5.jpg")
    with open(base_label + file_id + "_blur_1_rotated_cc_5.txt", "w") as f:
        f.write(label)

    #rotated_cc_5 = original_image.rotate(15)
    #rotated_cc_5.save(base + "/" + file_id + "_rotated_cc_15.jpg")
    with open(base_label + file_id + "_rotated_cc_15.txt", "w") as f:
        f.write(label)

    #rotated_cc_5 = original_image.rotate(100)
    #rotated_cc_5.save(base + "/" + file_id + "_rotated_cc_100.jpg")
    with open(base_label + file_id + "_rotated_cc_100.txt", "w") as f:
        f.write(label)

    #blur_5 = original_image.filter(ImageFilter.GaussianBlur(5))
    #blur_5.save(base + "/" + file_id + "_blur_5.jpg")
    #with open("data/train/labels/" + file_id + "_blur_5.txt", "w") as f:
    #    f.write(label)

    #blur_10 = original_image.filter(ImageFilter.GaussianBlur(10))
    #blur_10.save(base + "/" + file_id + "_blur_10.jpg")
    #with open("data/train/labels/" + file_id + "_blur_10.txt", "w") as f:
    #    f.write(label)

    #flipped_horizontal = blur_5.transpose(Image.FLIP_TOP_BOTTOM)
    #flipped_horizontal.save(base + "/" + file_id + "_flipped_h_blur_5.jpg")
    #with open("data/train/labels/" + file_id + "_flipped_h_blur_5.txt", "w") as f:
    #    f.write(label)

    #rotated_cc90 = original_image.transpose(Image.ROTATE_90)
    #rotated_cc90.save(base + "/" + file_id + "_rotated_cc90.jpg")
    #with open("data/train/labels/" + file_id + "_rotated_cc90.txt", "w") as f:
    #    f.write(label)
