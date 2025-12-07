from ultralytics import YOLO

def train(model: YOLO, train_path: str, epochs: int, img_size: int, batch_size: int):
    model.train(
        data=train_path,
        epochs=epochs,
        imgsz=img_size,
        batch=batch_size,
        augment=True
    )