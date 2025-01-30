import sys 
import logging
from datetime import datetime
import os
logs_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

Log_path = os.path.join(os.getcwd(),"logs",logs_file)

os.makedirs(Log_path,exist_ok=True)

Logs_file_path = os.path.join(Log_path,logs_file)

logging.basicConfig(
    filename=Logs_file_path,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
    )
