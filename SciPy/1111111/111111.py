from .. import dbConnection

fetch = dbConnection.doQuery("SELECT * FROM weather")
print(fetch)