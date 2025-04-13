# src/3_feature_engineering.py
def prepare_features(df):
    X = df[['Area', 'Bedrooms', 'Age']]  # Features
    y = df['Price']  # Target variable
    return X, y
