from ultralytics import YOLO

def create_model():
    model = YOLO("yolov8n-cls.pt")
    return model