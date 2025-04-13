# src/1_data_ingestion.py
import pandas as pd

def load_data():
    df = pd.read_csv('data/raw/dataset.csv')  # Load data from the 'raw' folder
    return df
