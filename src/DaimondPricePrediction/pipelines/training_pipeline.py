
from src.DaimondPricePrediction.components.data_ingestion import DataIngestion
from src.DaimondPricePrediction.components.preprocessing import DataTransformation
from src.DaimondPricePrediction.components.model_trainer import ModelTrainer


if __name__ == '__main__':
    data_ingestion_obj = DataIngestion()
    train_data_path,test_data_path = data_ingestion_obj.initiate_data_ingestion()

    preprocessing_object = DataTransformation()
    train_arr,test_arr = preprocessing_object.initiate_data_transformation(train_data_path,test_data_path)
    #print(train_arr.shape,test_arr.shape)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr,test_arr)



