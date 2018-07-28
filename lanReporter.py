'''
    This is the main app module, in charge of starting, parsing params and stopping.
    Each real functionnality lives in a separate module.
    Ultimately, thread management should be implemented in the orchestrator module.
'''

# Generic imports
#======================================================
# We will be running plenty of stuff at once...
import thread 

# This is the time I stop using prints everywhere :)
import logging



# Logging stuff
#======================================================
# The config module holds all app-wide parameters
import config

logging.basicConfig(format=config.LOG_FORMAT)
logger = logging.getLogger('LanNews')
logger.setLevel(config.LOG_LEVEL)
logger.debug('Running main file: %s' % __name__)

# Our own imports
#======================================================
# This is just a sample/template module to learn stuff or serve as a base:
import templateModule
# This will be the module in charge of giving orders to other modules and
# centralising feedback and available information.
#import orchestrator
# This will handle a web server/admin tool
#import webServer
# This will scan the LAN, looking for shares, computers and games
#import lanScanner
# This will be used to talk to the various game servers
#import gameQuery
# This will handle data persistance and db storage
#import dataStore
# This will handle displaying stuff
#import displayModule



if __name__ == '__main__':
    # Start the various threads
    try:
        # Run a sample thread, with an arg
        thread.start_new_thread( templateModule.main, ("plop",) )
    except Exception as e:
        logger.error('Could not start all threads')
        logger.error(e)

    # Main loop
    while 1:
       pass	# Do nothing for a long time.
       		# The only real-life skill school prepared you for.
