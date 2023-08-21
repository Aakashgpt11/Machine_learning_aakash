# for the logging purpose
# log track krne ke liye logger.py ko use krenge 

import logging
import os 
from datetime import datetime

# log_file ek text file hai jisme date aur time dono log rhega 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",LOG_FILE_PATH)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s ",
    level=logging.INFO
)

if __name__ =="__main__":
    logging.info("logging has started")

