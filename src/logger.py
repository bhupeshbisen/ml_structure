# This file help us at the time of production
import logging
import os
import sys

from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # It will create the log file with current running time

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # Find the path of current working directory

os.makedirs(logs_path,exist_ok=True) # It will create the logs folder if not exist

LOG_FILE_PATH= os.path.join(logs_path,LOG_FILE)



logging.basicConfig(
filename =LOG_FILE_PATH,
format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
level= logging.INFO, # Here we can set other logger levels[debug,info,warning,error,critical]
)
