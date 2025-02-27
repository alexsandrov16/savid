import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'SAViD.log',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

'''
def logs(level='debug', message=None):
    if level == 'debug':
        logging.debug(msg=message)
    if level == 'info':
        logging.info(msg=message)
    if level == 'warning':
        logging.warning(msg=message)
    if level == 'error':
        logging.error(msg=message)
    if level == 'critical':
        logging.critical(msg=message)
'''