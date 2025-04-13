from sklearn.metrics import r2_score

def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)
    print(f"Model R^2 Score: {score:.2f}")
    return score  # Return the score so that it can be used later
