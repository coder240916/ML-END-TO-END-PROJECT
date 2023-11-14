import pandas as pd
import numpy as np
import os
import pickle
import sys
import joblib

from src.DaimondPricePrediction.logger import logging
from src.DaimondPricePrediction.exceptions import CustomException
from pathlib import Path

from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import cross_val_score


def save_object_1(file_path:Path,obj:object):
    try:
        folder,file = os.path.split(file_path)
        Path(folder).mkdir(parents=True,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def save_object(file_path:Path,obj:object):
    try:
        folder,file = os.path.split(file_path)
        Path(folder).mkdir(parents=True,exist_ok=True)

        joblib.dump(obj,file_path)

    except Exception as e:
        raise CustomException(e,sys)

def load_pickle_object(file_path):
    try:
        # with open(file_path,'rb') as file_obj:
        #     return pickle.load(file_obj)
        return joblib.load(file_path)
    except Exception as e:
        logging.error("An Error occured while loading pickle file")
        raise CustomException(e,sys)
    

def evaluate_models(X_train,X_test,y_train,y_test,models):
    try:
        model_scores_df = pd.DataFrame(columns=['training_RMSE_Score',"CV_RMSE_mean_score","CV_RMSE_precision(std)"])

        for model_key in models:
            logging.info(f"Training model {models[model_key]}")
            model = models[model_key]

            model.fit(X_train,y_train)
            y_pred = model.predict(X_train)

            train_rmse_score = mse(y_train,y_pred,squared=False)

            logging.info("Performing 3 fold cross validation.")

            cross_val_rmses = -cross_val_score(model,
                                            X_train,
                                            y_train,
                                            cv=3,
                                            scoring="neg_root_mean_squared_error")
            
            cross_val_rmse_score = pd.Series(cross_val_rmses).mean()
            cross_val_score_std = pd.Series(cross_val_rmses).std()
            
            model_scores_df.loc[model_key] = [train_rmse_score,cross_val_rmse_score,cross_val_score_std]
        logging.info("Evaluation of all models completed.")
        return model_scores_df
    except Exception as e:
        logging.error("An error occured during model learning and cross validation.")
        raise CustomException(e,sys)
        

if __name__ == '__main__':
    save_object('artefacts/preprocessing_saved_obj.pkl','preprocessing')


