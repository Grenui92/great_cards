
import logging

def get_logger():
    """Return for the project. It is used to log information, warnings and errors.\
    'from tools.logger import logger'
    """
    return logging.getLogger('django')

logger = get_logger()
