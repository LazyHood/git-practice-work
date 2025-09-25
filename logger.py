import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

def log_with_timestamp(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}')
