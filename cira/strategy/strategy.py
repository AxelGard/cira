from typing import List
import pickle
import pandas as pd
import numpy as np
import random


class Strategy:
    def __init__(self, name) -> None:
        self.name = name

    def fit(self, train_data) -> None:
        raise NotImplementedError

    def predict(self, feature_data:pd.DataFrame, prices:pd.DataFrame, cash: float) -> np.ndarray:
        """
        Takes in feature data, then returns allocation prediction.
        """
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


class Randomness(Strategy):
    def __init__(self, lower: int = -1, upper: int = 1) -> None:
        super().__init__(name="Randomness")
        self.a = lower
        self.b = upper
        self.allocation = []

    def fit(self, train_data) -> None:
        pass

    def predict(self, feature_data, prices, cash: float) -> np.ndarray:
        al =  np.array(
            [random.randint(self.a, self.b) for _ in range(len(feature_data.keys()))]
        )
        self.allocation.append(al)
        return al


class ByAndHold(Strategy):
    def __init__(self) -> None:
        super().__init__(name="ByAndHold")
        self.is_first = True
        self.allocation = []

    def fit(self, train_data) -> None:
        pass

    def predict(self, feature_data, prices, cash: float) -> np.ndarray:
        if self.is_first:
            self.is_first = False
            amount = cash / len(prices.keys())
            amount *= 0.96
            al = (amount // prices.values).astype(np.int64)[0]
            self.allocation.append(al)
            return al
        al = np.array([0] * len(prices.keys()))
        self.allocation.append(al)
        return al
