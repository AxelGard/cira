from typing import List
import pickle
import pandas as pd
import numpy as np
import random
import schedule
import time


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


class Randomness(Strategy):
    def __init__(self, lower: int = -1, upper: int = 1, seed=0) -> None:
        super().__init__(name="Randomness")
        random.seed(seed)
        self.a = lower
        self.b = upper
        self.allocation = []

    def iterate(
        self,
        feature_data: pd.DataFrame,
        prices: pd.DataFrame,
        portfolio: np.ndarray,
        cash=float,
    ) -> np.ndarray:
        al = np.array(
            [random.randint(self.a, self.b) for _ in range(len(prices.keys()))]
        )
        self.allocation.append(al)
        return al


class ByAndHold(Strategy):
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
            amount *= 0.96
            al = (amount // prices.values).astype(np.int64)[0]
            self.allocation.append(al)
            return al
        al = np.array([0] * len(prices.keys()))
        self.allocation.append(al)
        return al


FEE_RATE = 0.004  # this is what alpaca takes

fees = lambda prices, allocation: FEE_RATE * np.matmul(prices.T, allocation)


def back_test(
    strat: Strategy,
    feature_data: pd.DataFrame,
    asset_prices: pd.DataFrame,
    capital=100_000.0,
    use_fees: bool = True,
) -> pd.DataFrame:
    """
    DISCLAIMER:
    The results of this backtest are based on historical data and do not guarantee future performance.
    The financial markets are inherently uncertain, and various factors can influence actual trading results.
    This backtest is provided for educational and informational purposes only.
    Users should exercise caution and conduct additional research before applying any trading strategy in live markets.
    """
    portfolio_history = {
        "value": [],
        "timestamp": [],
    }
    assert len(feature_data) == len(asset_prices)
    total_value = capital
    nr_of_asset = np.zeros([len(asset_prices.keys())], int)
    i = 0
    for t, cur_price in asset_prices.iterrows():
        if len(asset_prices) == i + 1:
            break
        if total_value > 0:
            f_data = feature_data.iloc[: i + 1]
            p_data = asset_prices.iloc[: i + 1]
            allocation = strat.iterate(f_data, p_data, nr_of_asset.copy(), capital)
            assert len(allocation) == len(
                nr_of_asset
            ), "tried to allocating more assets then is aviabel"
            for a, _ in enumerate(allocation):
                if capital <= 0.0 and allocation[a] < 0.0:
                    allocation[a] = 0
                if nr_of_asset[a] + allocation[a] < 0.0:
                    allocation[a] = -nr_of_asset[a]
            asking = float(
                np.matmul(cur_price.values.T, allocation)
                + use_fees * fees(cur_price.values, allocation)
            )  # - capital)
            if asking < capital:
                capital -= asking
                nr_of_asset += allocation
            total_value = np.matmul(cur_price.values.T, nr_of_asset) + capital
        else:
            total_value = np.matmul(cur_price.values.T, nr_of_asset) + capital

        portfolio_history["timestamp"].append(t)
        portfolio_history["value"].append(total_value)
        i += 1

    df = pd.DataFrame(portfolio_history)
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index.get_level_values("timestamp"))
    df.rename(columns={"value": strat.name}, inplace=True)
    return df


def multi_strategy_backtest(
    strats: List[Strategy],
    feature_data: pd.DataFrame,
    asset_prices: pd.DataFrame,
    capital=100_000.0,
    use_fees: bool = True,
):
    result = pd.DataFrame()
    result.index = asset_prices.index
    for s in strats:
        s_result = back_test(
            s,
            feature_data=feature_data,
            asset_prices=asset_prices,
            capital=capital,
            use_fees=use_fees,
        )
        result[s.name] = s_result[s.name]
    return result


def back_test_against_buy_and_hold(
    strat: Strategy,
    feature_data: pd.DataFrame,
    asset_prices: pd.DataFrame,
    capital=100_000.0,
    use_fees: bool = True,
):
    buy_and_hold = ByAndHold()
    return multi_strategy_backtest(
        strats=[strat, buy_and_hold],
        feature_data=feature_data,
        asset_prices=asset_prices,
        capital=capital,
        use_fees=use_fees,
    )


class Scheduler:
    def __init__(self) -> None:
        pass

    def add_daily_job(self, func_name) -> None:
        schedule.every(1).days.do(func_name)

    def add_daily_job_at(self, func_name, time_HM: str = "12:00") -> None:
        schedule.every().day.at(time_HM).do(func_name)

    def add_hour_job(self, func_name) -> None:
        schedule.every(1).hour.do(func_name)

    def add_minute_job(self, func_name) -> None:
        schedule.every(1).minute.do(func_name)

    def add_daily_job_at_time_EDT(self, func_name, time_HM: str = "12:00") -> None:
        schedule.every().day.at(time_HM, "America/New_York").do(func_name)

    def get_all_jobs(self):
        return schedule.jobs

    def clear_all_jobs(self) -> None:
        schedule.clear()

    def run(self):
        """runs the scheduler for ever"""
        while True:
            schedule.run_pending()
            time.sleep(1)
