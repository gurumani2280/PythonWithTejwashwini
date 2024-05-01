import logging
class Util :
    @staticmethod
    def getLogger(name=__name__):

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        c_handler = logging.StreamHandler()  # to print on console
        f_handler = logging.FileHandler('file.log')  # to print into file

        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        return logger