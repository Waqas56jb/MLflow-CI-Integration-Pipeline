# 🚀 main.py to run all steps
from src.1_data_ingestion import load_data
from src.2_data_preprocessing import preprocess
from src.3_feature_engineering import prepare_features
from src.4_model_training import train_model
from src.5_model_evaluation import evaluate

def main():
    df = load_data()
    df = preprocess(df)
    X, y = prepare_features(df)
    model, X_test, y_test = train_model(X, y)
    evaluate(model, X_test, y_test)

if __name__ == "__main__":
    main()
