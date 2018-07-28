'''
    This is the general config module
'''

# We need that for the debug level constants, but this module does not
# contain runnable code, just parameters.
import logging


#Logging related:
#======================================================
# Pick the app-wide log level:
LOG_LEVEL=logging.DEBUG
# Pick the app-wide log format:
LOG_FORMAT="<%(levelname)s> %(filename)s \t%(message)s"


# webServer module related:
#======================================================
WEBSERVER_PORT=8888


