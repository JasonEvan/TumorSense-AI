from ultralytics import YOLO
import os

def load_model():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "../outputs/models/best.pt")
    model = YOLO(model_path)
    return model