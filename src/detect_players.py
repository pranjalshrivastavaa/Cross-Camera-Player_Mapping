# src/detect_players.py
import cv2
from ultralytics import YOLO

def detect_players(video_path, model_path):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    players = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO model prediction
        results = model.predict(frame, save=False)  
        for result in results: 
            boxes = result.boxes  
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()  
                conf = box.conf[0].item()  
                cls = int(box.cls[0].item())  
                if cls == 0:  
                    players.append({
                        "frame": cap.get(cv2.CAP_PROP_POS_FRAMES),
                        "bbox": [x1, y1, x2, y2],
                        "confidence": conf
                    })

    cap.release()
    return players
