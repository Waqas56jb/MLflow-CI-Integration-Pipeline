from src.logger import setup_logger

logger = setup_logger("feature_engineering")

def prepare_features(df):
    logger.info("Preparing features and target")
    X = df[['Area', 'Bedrooms', 'Age']]
    y = df['Price']
    logger.info(f"Features shape: {X.shape}, Target shape: {y.shape}")
    return X, y

