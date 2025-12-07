from data_preprocess import preprocess_data
from model import create_model
from train import train
from evaluate import evaluate_model
import yaml

if __name__ == "__main__":
    with open('./../config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    preprocess_data()
    model = create_model()
    train(
        model, 
        train_path="./../data/brain-tumor-mri-dataset-yolo", 
        epochs=config['epochs'],
        img_size=config['img_size'],
        batch_size=config['batch_size']
    )
    evaluate_model(
        model,
        test_path='./../data/brain-tumor-mri-dataset/Testing'
    )
    model.save('./../outputs/models/best.pt')