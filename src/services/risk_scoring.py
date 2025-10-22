from sklearn.ensemble import RandomForestClassifier
import numpy as np

class RiskScoring:
    def __init__(self):
        # Initialize the model
        self.model = RandomForestClassifier()
        self.is_trained = False

    def train_model(self, X, y):
        # Train the model with provided features and labels
        self.model.fit(X, y)
        self.is_trained = True

    def predict_risk(self, features):
        # Predict risk score for given features
        if not self.is_trained:
            raise Exception("Model is not trained yet.")
        risk_score = self.model.predict_proba([features])[0][1]  # Probability of being in the risky class
        return risk_score

    def evaluate_route(self, crowd_density, lighting_quality, police_proximity, user_reports):
        # Example feature set for prediction
        features = np.array([crowd_density, lighting_quality, police_proximity, user_reports])
        return self.predict_risk(features)