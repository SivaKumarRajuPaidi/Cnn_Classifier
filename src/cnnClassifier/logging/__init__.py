import os
import sys
import logging

from datetime import datetime

logging_str = "[%(asctime)s; %(name)s; level:%(levelname)s; File_name:%(module)s; Line_No:%(lineno)d; %(message)s]"
log_dir = "logs"

log_filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_filepath = os.path.join(os.getcwd(),log_dir, log_filename)
os.makedirs(log_dir, exist_ok=True)




logging.basicConfig(
    # filename = LOG_FILE_PATH ,
    #format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    format = logging_str,
    level = logging.INFO,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")