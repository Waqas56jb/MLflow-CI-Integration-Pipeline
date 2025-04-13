from src.logger import setup_logger
import yaml

logger = setup_logger("data_preprocessing")
with open("params.yaml") as f:
    params = yaml.safe_load(f)

def preprocess(df):
    if params['preprocessing']['dropna']:
        logger.info("Dropping missing values")
        df = df.dropna()
    logger.info(f"Data after preprocessing: {df.shape}")
    return df
