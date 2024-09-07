import os
from ultralytics import YOLO
import cv2
import numpy as np

model_path = "best1.pt"  
image_path = "Speedbreaker1.jpeg"  # Replace with the path to your image

model = YOLO(model_path)

results = model.predict(source=image_path)

result_image = results[0].plot()

image_bgr = cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR)

cv2.imshow('Detected Image', image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
