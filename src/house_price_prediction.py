import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    # Load data
    data = pd.read_csv('data/dataset.csv')

    X = data[['Area', 'Bedrooms', 'Age']]
    y = data['Price']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model R^2 Score: {score:.2f}")

if __name__ == "__main__":
    main()
