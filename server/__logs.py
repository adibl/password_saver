import logging
import logging.config
import os

LOGGER_NAME = 'sss'
LOG_FILE = 'logs/API.log'
CONF_FILE = 'log.ini'


def setup_logging():
    """
    Setup logging configuration
    """
    path = CONF_FILE
    if os.path.exists(path):
        logging.config.fileConfig(path)


def handle_logging():
    """
    create tread that listen and auto-cange log config on run
    :return: tread object
    """
    setup_logging()
    logging.info('start logging changes server')
    return logging.config.listen(9999).start()
