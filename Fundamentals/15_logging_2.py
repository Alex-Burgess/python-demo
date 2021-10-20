'''
Advanced logging - loggers
'''
import logging
import employee

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('Fundamentals/test.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('Confirmation that things are working as expected.')
