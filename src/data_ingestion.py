import pandas as pd
from src.logger import setup_logger

logger = setup_logger("data_ingestion")

def load_data():
    logger.info("Loading dataset...")
    df = pd.read_csv('data/raw/dataset.csv')
    logger.info(f"Dataset loaded with shape: {df.shape}")
    return df