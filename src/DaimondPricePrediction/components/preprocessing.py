import pandas as pd
import numpy as np
import sys

from pathlib import Path
from dataclasses import dataclass

from src.DaimondPricePrediction.utils.utils import save_object
from src.DaimondPricePrediction.logger import logging
from src.DaimondPricePrediction.exceptions import CustomException

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer,make_column_selector


# it is a oridinal encoding
cut_categories=["Fair","Good","Very Good","Premium","Ideal"]
clarity_categories = ["I1","SI2","SI1","VS2", "VS1" , "VVS2" , "VVS1" ,"IF"]
color_categories = ["D" ,"E" ,"F" , "G" ,"H" , "I", "J"]


@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path = Path("artifacts/preprocessing.pkl")



class DataTransformation:
    
    def __init__(self):
        self.transformation_config = DataTransformationConfig()
    
    def get_transformation_object(self):
        try:
            num_pipeline = Pipeline([("impute",SimpleImputer(strategy='mean')),
                            ("scaler",StandardScaler())])
            
            cat_pipeline = Pipeline([("impute",SimpleImputer(strategy='most_frequent')),
                ("encoder",OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                            ("scaler",StandardScaler())])
            
            preprocessing = ColumnTransformer([
                                                ('num',num_pipeline,make_column_selector(dtype_include='float')),
                                                ("cat",cat_pipeline,make_column_selector(dtype_include="object"))
                                            ])
            return preprocessing
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Data Transformation started.")

            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            logging.info("Reading Train and Test data completed.")

            target_feature = 'price'

            train_data_input_feature_df = train_data.drop([target_feature],axis=1)
            train_data_target_feature_df = train_data[target_feature]

            test_data_input_feature_df = test_data.drop([target_feature],axis=1)
            test_data_target_feature_df = test_data[target_feature]

            logging.info("Train and Test data input features and target seperated to dataframes.")
            
            logging.info("Getting data transformation object.")

            preprocessor = self.get_transformation_object()

            logging.info("Preprocessor object loaded.")

            train_data_input_arr = preprocessor.fit_transform(train_data_input_feature_df)
            test_data_input_arr  = preprocessor.transform(test_data_input_feature_df)

            logging.info("processing completed on train and test data.")

            # print(pd.DataFrame(data = train_data_input_arr,columns=preprocessor.get_feature_names_out(),index=train_data_input_feature_df.index))

            train_arr = np.c_[train_data_input_arr,np.array(train_data_target_feature_df)]
            test_arr = np.c_[test_data_input_arr,np.array(test_data_target_feature_df)]

            save_object("artifacts/preprocessing_object_saved.pkl",preprocessor)

            logging.info("preprocessing pickle file saved to artifacts directoty.")

            return (train_arr,
                    test_arr)
        except Exception as e:
            logging.error("Unexpected error occured during data transformation")
            raise CustomException(e,sys)

if __name__ == "__main__":

    preprocessing_object = DataTransformation()
    train_arr,test_arr = preprocessing_object.initiate_data_transformation('artifacts/test_data.csv','artifacts/train_data.csv')
    # print(test_arr[0],test_arr[0])
    # print(train_arr[:,-1].shape,train_arr[:,-1].shape)



