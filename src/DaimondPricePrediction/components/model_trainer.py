import pandas as pd
import numpy as np
import sys
import os
import joblib

from pathlib import Path
from dataclasses import dataclass

from src.DaimondPricePrediction.utils.utils import save_object,evaluate_models
from src.DaimondPricePrediction.logger import logging
from src.DaimondPricePrediction.exceptions import CustomException


from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor



@dataclass
class ModelTrianerConfiguration:
    model_file_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    
    def __init__(self):
        self.model_trainer_config = ModelTrianerConfiguration()

    def initiate_model_training(self,train_arr,test_arr):
        try:

            logging.info("Preparing train and test data for passing to learning models.")

            X_train,X_test,y_train,y_test = (train_arr[:,:-1],test_arr[:,:-1],train_arr[:,-1],test_arr[:,-1])

            logging.info("Splitting train and test data completed.")

            models = { 
                        'lin_reg':LinearRegression(),
                        'ridge':Ridge(alpha=0.1),
                        'lasso':Lasso(alpha=1),
                        'elastic_net':ElasticNet(),
                        'tree':DecisionTreeRegressor(),
                        #'random_forest':RandomForestRegressor()
                    }
            
            eval_report_df = evaluate_models(X_train,X_test,y_train,y_test,models)

            logging.info(eval_report_df.to_string())
            logging.info("Selecting best model based on cross validation scores.")

            models_sorted = eval_report_df.sort_values(by=['CV_RMSE_mean_score','training_RMSE_Score'],ascending=[True,True])
            best_model = models[models_sorted.index[0]]

            logging.info("Best model among the trained models.")
            logging.info(f"{best_model}")
            logging.info("\n"+models_sorted.iloc[0].to_string())

            save_object(self.model_trainer_config.model_file_path,best_model)
            logging.info("saved best model to artifacts directory. ")

        except Exception as e:
            logging.error("An error occured during model training.")
            raise CustomException(e,sys)
        

if __name__ == '__main__':
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training()








        

