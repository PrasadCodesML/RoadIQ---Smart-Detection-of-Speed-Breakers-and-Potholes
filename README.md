# RoadIQ : Smart Detection of Speed Breakers and Potholes 
Here we are doing Speed Breaker and Pothole detection using Iot and ML
This project demostrated a very good application Machine Learning integrating it with Internet of Things 

# Technical Approach 
Here I finetuned Yolo-v8 Instance Semgentation model - "yolov8s-seg.pt" which is a pretrained Instance Segmentation model on various common things, this model was finetuned to do instance segmentation of Potholes and Speedbreakers
The Input of Image of road was taken from ESP32 Camera module 
This image input was sent to the Trained segmentation model and this data was sent to Firebase
The second input was taken by the tilt sensor and this data was also sent to firebase using NodeMCU

# Software requirements :
1. **CNN** architecture for Image detection
2. **Python** for taking the image/video
3. **Firebase** for database of data regarding **tilt sensor**
4. Firebase for storing the coordinates of the road anomalies
5. **Arduino IDE** for tilt sensor working and pushing the coordinates of road to the database 
6. **HTML, CSS, Javascript** for interface
7. **Mapbox API** for map integration with interface
8. **Google Colab** for training the model
9. **Google API** for fetching coordinates of that location

# Hardware requirements :
1. Node MCU
2. Tilt Sensor
3. Buzzer
4. **ESP32 camera module**
