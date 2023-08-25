import cv2
from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO("yolov8n.pt")

image = Image.open("raw_data/2511.png")
image = np.asarray(image)

results = model.predict(image)