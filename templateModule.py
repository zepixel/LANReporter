'''
    This is a sample submodule to serve as a template or to try things out.
    Copy it to new files to create other modules
'''

# This is the time I stop using prints everywhere :)
import logging

# Turns out for more control, "thread" will have to be replaced with "threading"
import thread


# Seems reconfiguring logging in submodules is not necessary when using a named logger
# (see : https://docs.python.org/2/howto/logging.html#logging-from-multiple-modules)
#logging.basicConfig()
#logger = logging.getLogger('LanNews')
#logger.setLevel(logging.DEBUG)

# Use the common logger
logger = logging.getLogger('LanNews')
logger.debug('Loaded %s module' % __name__)

# The main function that will be called from the main thread manager
def main(sampleArg):
    logger.debug('Started main() function')
    # Main loop
    logger.debug('Argument I got is "%s" ' % sampleArg )
    while 1:
        leaveModule()
        pass

# The function containing all the cleanup for a proper module leave.
def leaveModule():
    logger.debug('We have been asked to leaveModule()...')

   # [...] do actual cleanup here

    # Kthxbye.
    logger.debug('Exiting %s module' % __name__)
    # don't use exit() here: it would kill the whole app,and not just the thread :)
    thread.exit()

