# src/utils.py
import cv2

def draw_bounding_boxes(frame, players):
    for player in players:
        x1, y1, x2, y2 = player['bbox']
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {player['id']}", (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
