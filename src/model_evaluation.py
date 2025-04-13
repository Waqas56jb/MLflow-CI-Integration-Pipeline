from sklearn.metrics import r2_score
from src.logger import setup_logger

logger = setup_logger("model_evaluation")

def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)
    logger.info(f"Model R^2 Score: {score:.2f}")
    with open("evaluation_results.txt", "w") as f:
        f.write(f"R2 Score: {score:.2f}\n")
    return score