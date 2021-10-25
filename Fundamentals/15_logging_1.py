###################################
# Logging
#
# Logging in python is built in, you just need to import the package.
###################################
import logging

# By default it logs all messages of warning severity or higher.  The level can be changed.
# logging.basicConfig(level=logging.DEBUG)

# By default it logs all messages to the console.  This can be changed to file.
# logging.basicConfig(filename='Fundamentals/test.log', level=logging.DEBUG)

# Change the format
# e.g. 2021-10-20 15:04:03,680:DEBUG:Detailed information, typically of interest only when diagnosing a problem.
logging.basicConfig(filename='Fundamentals/test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

logging.debug('Detailed information, typically of interest only when diagnosing a problem.')
logging.info('Confirmation that things are working as expected.')
logging.warning('An indication that something unexpected happened, or indicative of some problem in the near future (disk space low, deprecation, etc).  The software is still working as expected.')
logging.error('Due to a more serious problem, the software has not been able to perform some function.')
logging.critical('A serious error, indicating that the program itself may be unable to continue running.')
