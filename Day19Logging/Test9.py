from util import Util
def test_logger():
    logger = Util.getLogger(__name__)
    logger.warning('%s This will get logged to a file',__name__)
    logger.debug('This is debug message')
    logger.info('I told you so')  # will not print anything
    logger.warning('Watch out!')  # will print a message to the console
    logger.error('This is an error message')
    logger.critical('This is a critical message')


def test_logger2():
    logger = Util.getLogger(__name__)
    logger.warning('%s This will get logged to a file',__name__)
    logger.debug('This is debug message')
    logger.info('I told you so')  # will not print anything
    logger.warning('Watch out!')  # will print a message to the console
    logger.error('This is an error message')
    logger.critical('This is a critical message')
