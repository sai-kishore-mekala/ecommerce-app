import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(service_name):
    log_dir = "/var/log/app"
    os.makedirs(log_dir, exist_ok=True)

    log_path = f"{log_dir}/{service_name}.log"
    
    logger = logging.getLogger(service_name)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

