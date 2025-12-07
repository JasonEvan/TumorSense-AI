import os
import shutil
import random

def preprocess_data():
    # LOAD TRAINING AND VALIDATION DATASET
    root_dir = "./../data/brain-tumor-mri-dataset/Training"
    classes = ["glioma", "meningioma", "notumor", "pituitary"]

    # path tujuan
    out_dir = "./../data/brain-tumor-mri-dataset-yolo"
    splits = ["train", "val"]
    ratios = [0.7, 0.3]  # 70% train, 30% val

    # buat folder tujuan
    for split in splits:
        for cls in classes:
            dir_path = os.path.join(out_dir, split, cls)
            os.makedirs(dir_path, exist_ok=True)

    # proses tiap kelas
    for cls in classes:
        files = os.listdir(os.path.join(root_dir, cls))
        random.shuffle(files)

        n_total = len(files)
        n_train = int(ratios[0] * n_total)
        n_val   = int(ratios[1] * n_total)

        train_files = files[:n_train]
        val_files   = files[n_train:n_train+n_val]

        for f in train_files:
            shutil.copy(
                os.path.join(root_dir, cls, f),
                os.path.join(out_dir, "train", cls, f)
            )
        for f in val_files:
            shutil.copy(
                os.path.join(root_dir, cls, f),
                os.path.join(out_dir, "val", cls, f)
            )

    # LOAD TEST DATASET
    root_dir = "./../data/brain-tumor-mri-dataset/Testing"
    classes = ["glioma", "meningioma", "notumor", "pituitary"]

    # path tujuan
    out_dir = "./../data/brain-tumor-mri-dataset-yolo"
    splits = ["test"]

    # buat folder tujuan
    for split in splits:
        for cls in classes:
            dir_path = os.path.join(out_dir, split, cls)
            os.makedirs(dir_path, exist_ok=True)

    # proses tiap kelas
    for cls in classes:
        files = os.listdir(os.path.join(root_dir, cls))
        random.shuffle(files)

        for f in files:
            shutil.copy(
                os.path.join(root_dir, cls, f),
                os.path.join(out_dir, "test", cls, f)
            )