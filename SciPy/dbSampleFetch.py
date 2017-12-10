# A simple example of printing out the data from a database, specified in the databaseConfig.py

import dbConnection
from .. import test2

fetch = dbConnection.doQuery("SELECT * FROM weather")
print (fetch)
print (test2.out)