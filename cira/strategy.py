import pickle
import numpy as np

class Strategy: 
    def __init__(self) -> None: 
        pass

    def fit(self, X_train:np.ndarray, y_train:np.ndarray) -> None:
        raise NotImplementedError

    def predict(self,  X_test:np.ndarray) -> np.ndarray: 
        raise NotImplementedError

    def size_position(self, entry_price) -> int:
        raise NotImplementedError

    
    def save(self, file_path):
        """
        Save model to pickle file 
        usage: 
            model.train(X_train, y_train)
            model.save('./model.pkl')
        """
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, file_path):
        """
        Load in model from pickle file
        usage: 
            model = Strategy.load('./model.pkl')
            predictions = model.predict(X_test)
        """
        with open(file_path, 'rb') as file:
            return pickle.load(file)