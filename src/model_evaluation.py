# src/5_model_evaluation.py
from sklearn.metrics import r2_score

def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)
    print(f"Model R^2 Score: {score:.2f}")
