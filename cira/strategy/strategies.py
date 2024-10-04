from cira.strategy import strategy
import random
import numpy as np
import pandas as pd
import typing


class Randomness(strategy.Strategy):
    """An example strategy that buy and sells at random for each available asset"""

    def __init__(
        self,
        lower: float = -1,
        upper: float = 1,
        seed=0,
        use_float: bool = False,
    ) -> None:
        super().__init__(name="Randomness")
        random.seed(seed)
        self.a = lower
        self.b = upper
        self.allocation = []
        self.use_float = use_float

    def iterate(
        self,
        feature_data: pd.DataFrame,
        prices: pd.DataFrame,
        portfolio: np.ndarray,
        cash=float,
    ) -> np.ndarray:
        al = np.array(
            [
                random.uniform(float(self.a), float(self.b))
                for _ in range(len(prices.keys()))
            ]
        )
        if not self.use_float:
            al = al.astype(int)
        self.allocation.append(al)
        return al


class DollarCostAveraging(strategy.Strategy):
    """An example strategy that always buys a set amount of all assets for each iteration"""

    def __init__(self, amount: typing.Union[float, int] = 1) -> None:
        super().__init__(name="DollarCostAveraging")
        self.amount = amount
        self.allocation = []

    def iterate(
        self,
        feature_data: pd.DataFrame,
        prices: pd.DataFrame,
        portfolio: np.ndarray,
        cash=float,
    ) -> np.ndarray:
        al = np.array([self.amount for _ in range(len(prices.keys()))])
        self.allocation.append(al)
        return al


class BuyAndHold(strategy.Strategy):
    """An example strategy that buys as much as possible of each asset on the first iteration then holds"""

    def __init__(self) -> None:
        super().__init__(name="BuyAndHold")
        self.is_first = True
        self.allocation = []

    def iterate(
        self,
        feature_data: pd.DataFrame,
        prices: pd.DataFrame,
        portfolio: np.ndarray,
        cash=float,
    ) -> np.ndarray:
        if self.is_first:
            self.is_first = False
            amount = cash / len(prices.keys())
            amount *= 0.96  # fees
            al = (amount // prices.values).astype(np.int64)[0]
            self.allocation.append(al)
            return al
        al = np.array([0] * len(prices.keys()))
        self.allocation.append(al)
        return al
