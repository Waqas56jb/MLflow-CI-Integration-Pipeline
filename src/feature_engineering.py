def prepare_features(df):
    X = df[['Area', 'Bedrooms', 'Age']]
    y = df['Price']
    return X, y