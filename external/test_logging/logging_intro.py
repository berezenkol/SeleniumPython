"""
Logging - we print statements in order to say app is doing smt. If something goes wrong, people can read the
log and has a chance to figure out what happened. Likewise, test_logging is important for system developing,
debugging and running. When a program crashes, if there is no test_logging record, you have little chance to understand what happened.
print() - prints statements only to the console. Logging - we can log to the files.

Logging levels:
DEBUG - when we debugging smt, when we diagnost problems
INFO  - confirmation of things that it is working as expected
WARNING    - by default the threshold is set to warning , smt unexpected happen (or may happen in the future), but software is still working aas expected
ERROR   - more serious problem, software is not able to perform as expected
CRITICAL   - most serious error, smt critical happen, programm is unable to continue to run

This moule is by default available in Python


"""

import logging

# statements above warning(incl.waring) are gonna be printed
# these statements are gonna be printed to the console only
# test_logging.warning('warning message')
# test_logging.info('info message')
# test_logging.error('error message')

# how to put statements to the file
# after running the code, the file 'test.log' is to be created & 3 statements to be written inside the file
logging.basicConfig(filename='test.log',level=logging.DEBUG)
logging.warning('warning message')
logging.info('info message')
logging.error('error message')