import os
import sys
import pandas as pd

from pathlib import Path

from src.DaimondPricePrediction.logger import logging
from src.DaimondPricePrediction.exceptions import CustomException
from src.DaimondPricePrediction.utils.utils import load_pickle_object


class PredictionObject:
    def __init__(self) -> None:
        pass

    def predict_data(self,features):
        try:
            preprocessing_path = Path("artifacts") / Path("preprocessing_object_saved.pkl")
            model_path = Path("artifacts") / Path("model.pkl")

            preprocessing_obj = load_pickle_object(preprocessing_path)
            model = load_pickle_object(model_path)

            features_scaled = preprocessing_obj.transform(features)
            predicted_data = model.predict(features_scaled)

            return predicted_data
        except Exception as e:
            logging.info("An error occured while predicting the data")
            raise CustomException(e,sys)
    

class CustomData:
    def __init__(self,carat, depth, table, x, y, z, cut, color, clarity):
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            data = [[self.carat,self.depth,self.table,self.x,self.y,self.z,self.cut,self.color,self.clarity]]
            columns = ['carat', 'depth', 'table', 'x', 'y', 'z', 'cut', 'color', 'clarity',]
            data_df = pd.DataFrame(data,columns=columns)
            logging.info("dataframe created from data")
            return data_df
        except Exception as e:
            raise CustomException(e,sys)
    

if __name__ == "__main__":
    prediction_obj = PredictionObject()
    data = CustomData(1.52, 62.2, 58.0, 7.27, 7.33, 4.55,'Premium', 'F', 'VS2')
    data_df = data.get_data_as_dataframe()
    predicted = prediction_obj.predict_data(data_df)
    print(f"Predicted value is {predicted}")




