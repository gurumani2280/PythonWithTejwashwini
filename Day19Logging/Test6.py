# logging_example.py

import logging
name = __name__
# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()   # to print on console
f_handler = logging.FileHandler('file.log')    # to print into file
# c_handler.setLevel(logging.INFO)
# f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('%s This will get logged to a file',name)
logger.debug('This is debug message')
logger.info('I told you so')  # will not print anything
logger.warning('Watch out!')  # will print a message to the console
logger.error('This is an error message')
logger.critical('This is a critical message')
