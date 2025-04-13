from src.data_ingestion import load_data
from src.data_preprocessing import preprocess
from src.feature_engineering import prepare_features
from src.model_training import train_model
from src.model_evaluation import evaluate

def main():
    # Data loading and preprocessing
    df = load_data()
    df = preprocess(df)
    X, y = prepare_features(df)
    
    # Processed data
    df_processed = df[['Area', 'Bedrooms', 'Age', 'Price']]  # Prepare processed data
    df_processed.to_csv('data/processed/processed.csv', index=False)  # Save processed data
    
    # Train model
    model, X_test, y_test = train_model(X, y)
    
    # Evaluate model and save results
    score = evaluate(model, X_test, y_test)
    
    # Write evaluation results to file
    with open('evaluation_results.txt', 'w') as f:
        f.write(f"Model R^2 Score: {score:.2f}")

if __name__ == "__main__":
    main()
