from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("best1.pt")
class_names = model.names
cap = cv2.VideoCapture(0)  # Use default camera (index 0)

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (1020, 500))
    h, w, _ = img.shape
    results = model.predict(img)

    if results:
        for r in results:
            boxes = r.boxes  # Boxes object for bbox outputs

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                cls_id = int(box.cls)
                conf = box.conf
                label = f"{class_names[cls_id]} {conf:.2f}"
                color = (0, 255, 0)  # Green color for bounding box

                # Draw the bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                # Put the label above the bounding box
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
