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


def handle_logging():
    """
    create tread that listen and auto-cange log config on run
    :return: tread object
    """
    # FIXME: move to __logs file
    setup_logging()
    logging.info('start logging changes server')
    return logging.config.listen(9999).start()
