import os

from pathlib import Path

package_name = "DaimondPricePrediction"

filepaths = [
            ".github/workflows/.gitkeep",
            "notebooks/research.ipynb",
            "notebooks/data/.gitkeep",
            f"src/{package_name}/components/__init__.py",
            f"src/{package_name}/components/data_ingestion.py",
            f"src/{package_name}/components/preprocessing.py",
            f"src/{package_name}/components/model_trainer.py",
            f"src/{package_name}/pipelines/__init__.py",
            f"src/{package_name}/pipelines/training_pipeline.py",
            f"src/{package_name}/pipelines/prediction_pipeline.py",
            f"src/{package_name}/exceptions.py",
            f"src/{package_name}/logger.py",
            f"src/{package_name}/__init__.py",
            f"src/{package_name}/utils/__init__.py",
            f"src/{package_name}/utils/utils.py",

            "requirements.txt",
            "setup.py",
            "init_setup.sh"
             ]

for filepath in filepaths:
    folder,file = os.path.split(filepath)

    if folder != "":
        Path(folder).mkdir(parents=True,exist_ok=True)

    if not os.path.exists(filepath):
        with open(filepath,'w') as f:
            pass
    else:
        print("file already exists!") 