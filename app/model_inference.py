from ultralytics import YOLO
from PIL import ImageFile

def predict(model: YOLO, input_data: ImageFile):
    results = model.predict(input_data)

    top_class_idx = results[0].probs.top1
    top_class_name = results[0].names[top_class_idx]

    return top_class_name