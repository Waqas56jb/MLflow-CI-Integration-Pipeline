from src.data_ingestion import load_data
from src.data_preprocessing import preprocess
from src.feature_engineering import prepare_features
from src.model_training import train_model
from src.model_evaluation import evaluate
from src.logger import setup_logger

logger = setup_logger("main")

def main():
    logger.info("Pipeline started")
    df = load_data()
    df = preprocess(df)
    X, y = prepare_features(df)
    model, X_test, y_test = train_model(X, y)
    score = evaluate(model, X_test, y_test)
    logger.info(f"Pipeline completed with R2 Score: {score:.2f}")

if __name__ == "__main__":
    main()