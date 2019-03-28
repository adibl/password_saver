GENERAL_ERROR = 500
DUPLIKATE_KEY_ERROR = 442
import logging
import pymongo.errors


from functools import wraps
def handle_general_eror(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            return f(*args, **kwds)
        except pymongo.errors.DuplicateKeyError as err:
            logging.debug('ID already exzist')
            return DUPLIKATE_KEY_ERROR
        except pymongo.errors as err:
            logging.info('server eror: ' + str(err))
            return GENERAL_ERROR

    return wrapper
