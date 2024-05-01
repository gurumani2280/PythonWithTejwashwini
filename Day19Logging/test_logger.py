from util import Util
class TestLogger :
    def test_logger3(self):
        logger = Util.getLogger(TestLogger.test_logger3.__name__)
        logger.warning('%s This will get logged to a file',__name__)
        logger.debug('This is debug message')
        logger.info('I told you so')  # will not print anything
        logger.warning('Watch out!')  # will print a message to the console
        logger.error('This is an error message')
        logger.critical('This is a critical message')


    def test_logger4(self):
        logger = Util.getLogger(TestLogger.test_logger4.__name__)
        logger.warning('%s This will get logged to a file',__name__)
        logger.debug('This is debug message')
        logger.info('I told you so')  # will not print anything
        logger.warning('Watch out!')  # will print a message to the console
        logger.error('This is an error message')
        logger.critical('This is a critical message')
