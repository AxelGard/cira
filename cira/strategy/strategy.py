import pickle
import pandas as pd
import numpy as np


class Strategy:
    def __init__(self, name) -> None:
        self.name = name

    def iterate(
        self,
        feature_data: pd.DataFrame,
        prices: pd.DataFrame,
        portfolio: np.ndarray,
        cash=float,
    ) -> np.ndarray:
        """
        Takes in feature data, then returns allocation prediction.
        """
        raise NotImplementedError

    def save(self, file_path):
        """
        Save strategy to pickle file
        usage:
            strategy.fit(train_data)
            strategy.save('./model.pkl')
        """
        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, file_path):
        """
        Load in strategy from pickle file
        usage:
            strategy = Strategy.load('./model.pkl')
            predictions = strategy.predict(test_data)
        """
        with open(file_path, "rb") as file:
            return pickle.load(file)
