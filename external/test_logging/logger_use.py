

import logging

class LoggerConsole():
    def testLog(self):

# printing statements to the console

#1. Create Logger and Set the level of the Logger
# Logger looks at the message and will create the Log record object from the message string, then will pass it to the handler

        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.INFO)

#2. Create Console Handler and set level to INFO
# Handler - is responsible for the output of messages to the console/to the file
# StreamHandle() -> prints to the console

        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

#3. Create Formatter
# Formatter - this will format log record object all the messages in the desired format and return to the handler

        formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

#4. Add Formatter to Console Handler -> ch
        chandler.setFormatter(formatter)

#5. Add Console Handler to Logger
        logger.addHandler(chandler)

# Logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical error')

d = LoggerConsole()
d.testLog()