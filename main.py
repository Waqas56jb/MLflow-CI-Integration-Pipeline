# 🚀 main.py to run all steps
from src.data_ingestion import load_data
from src.data_preprocessing import preprocess
from src.feature_engineering import prepare_features
from src.model_training import train_model
from src.model_evaluation import evaluate

def main():
    df = load_data()
    df = preprocess(df)
    X, y = prepare_features(df)
    
    # Processed data
    df_processed = df[['Area', 'Bedrooms', 'Age', 'Price']]  # Prepare processed data
    df_processed.to_csv('data/processed/processed.csv', index=False)  # Save processed data
    
    model, X_test, y_test = train_model(X, y)
    evaluate(model, X_test, y_test)

if __name__ == "__main__":
    main()