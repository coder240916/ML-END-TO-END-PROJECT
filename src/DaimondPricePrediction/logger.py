import logging
import os
from pathlib import Path
from datetime import datetime

LOG_FILE = f'''{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'''

log_path = os.getcwd() / Path("logs")

log_path.mkdir(exist_ok=True,parents=True)

LOG_FILE_PATH = log_path / Path(LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
                    level=logging.INFO,
                    format = "%(asctime)s [%(filename)s %(lineno)d] -%(levelname)s -%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
               
logger = logging.getLogger("project_logger")

if __name__ == '__main__':
    logger.info('this is a test message')