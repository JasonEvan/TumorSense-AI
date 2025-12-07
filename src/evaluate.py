from ultralytics import YOLO
import os
import numpy as np

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report

def evaluate_model(model: YOLO, test_path: str):
    image_paths = []
    class_names = sorted(os.listdir(test_path))

    for class_name in class_names:
        class_dir = os.path.join(test_path, class_name)
        for fname in os.listdir(class_dir):
            image_paths.append(os.path.join(class_dir, fname))


    results = model.predict(image_paths, save=False)

    y_pred = np.array([r.probs.top1 for r in results])
    y_true = []
    for class_idx, class_name in enumerate(class_names):
        folder = os.path.join(test_path, class_name)
        y_true.extend([class_idx] * len(os.listdir(folder)))

    y_true = np.array(y_true)

    print(f"accuracy: {accuracy_score(y_true, y_pred)}")
    print(f"recall: {recall_score(y_true, y_pred, average='macro')}")
    print(f"precision: {precision_score(y_true, y_pred, average='macro')}")
    print(f"f1: {f1_score(y_true, y_pred, average='macro')}")

    print("\nClassification Report:\n")
    print(classification_report(y_true, y_pred))