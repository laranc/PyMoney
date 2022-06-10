# errorhandler.py

from email import message

# general db handling
class databaseCreateError(Exception):
    pass

class databaseConnectionError(Exception):
    pass

# query handling
class databaseQueryFailed(Exception):
    pass