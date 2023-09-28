from typing import List
import pickle
import numpy as np


class Strategy:
    def __init__(self) -> None:
        pass

    def fit(self, train_data: np.array) -> None:
        raise NotImplementedError

    def predict(self, data: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def size(
        self,
        entry_price: float,
        prediction: np.ndarray,
        current_position: int,
        cash: float,
    ) -> int:
        raise NotImplementedError

    def get_features_names(self) -> List[str]:
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
