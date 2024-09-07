import os
from ultralytics import YOLO
import cv2

model_path = "best1.pt"  
video_path = "4.mp4"  
output_path = "4_output_video.mp4"  

model = YOLO(model_path)

cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame)

    result_image = results[0].plot()

    image_bgr = cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR)

    out.write(image_bgr)

    cv2.imshow('Detected Frame', image_bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
