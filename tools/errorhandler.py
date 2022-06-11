# errorhandler.py

from email import message

# general db handling
class database_create_error(Exception):
    pass

class database_connection_error(Exception):
    pass

# query handling
class database_query_failed(Exception):
    pass