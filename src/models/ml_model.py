from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd

class RiskScoringModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, X, y):
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True

    def predict(self, X):
        if not self.is_trained:
            raise Exception("Model must be trained before predictions can be made.")
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def save_model(self, filepath):
        joblib.dump((self.model, self.scaler), filepath)

    @classmethod
    def load_model(cls, filepath):
        model, scaler = joblib.load(filepath)
        instance = cls()
        instance.model = model
        instance.scaler = scaler
        instance.is_trained = True
        return instance

    def evaluate(self, X, y):
        if not self.is_trained:
            raise Exception("Model must be trained before evaluation can be performed.")
        X_scaled = self.scaler.transform(X)
        return self.model.score(X_scaled, y)