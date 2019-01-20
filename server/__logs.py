import logging
import logging.config
import yaml
import os

LOGGER_NAME = 'sss'
LOG_FILE = 'logs/API.log'
CONF_FILE = 'log.yaml'

def setup_logging():
    """
    Setup logging configuration
    """
    path = CONF_FILE
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)