import logging
import yaml
LOGGER_NAME = 'sss'
LOG_FILE = 'logs/API.log'
CONF_FILE = 'log.yaml'

import os
import logging.config

import yaml

def setup_logging(env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = CONF_FILE
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)