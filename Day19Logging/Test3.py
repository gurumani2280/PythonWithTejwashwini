import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
logging.warning('This will get logged to a file')
logging.debug('This is debug message')
logging.info('I told you so')  # will not print anything
logging.warning('Watch out!')  # will print a message to the console
logging.error('This is an error message')
logging.critical('This is a critical message')