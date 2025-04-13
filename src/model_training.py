from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import yaml
from src.logger import setup_logger

logger = setup_logger("model_training")
with open("params.yaml") as f:
    params = yaml.safe_load(f)

def train_model(X, y):
    test_size = params['model']['test_size']
    logger.info(f"Splitting data with test_size={test_size}")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    model = LinearRegression()
    model.fit(X_train, y_train)
    logger.info("Model trained successfully")
    joblib.dump(model, 'models/model.pkl')
    logger.info("Model saved to models/model.pkl")
    return model, X_test, y_test