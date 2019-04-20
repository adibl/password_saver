GENERAL_ERROR = 500
DUPLIKATE_KEY_ERROR = 442
ERRORS = [GENERAL_ERROR, DUPLIKATE_KEY_ERROR]
import logging
from functools import wraps

import pymongo.errors


def handle_general_eror(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            return f(*args, **kwds)
        except pymongo.errors.DuplicateKeyError as err:
            logging.debug('ID already exzist')
            return DUPLIKATE_KEY_ERROR
        except pymongo.errors.ConnectionFailure, e:
            logging.info("Could not connect to server: %s" % e)
        except pymongo.errors as err:
            logging.info('server eror: ' + str(err))
            return GENERAL_ERROR

    return wrapper
