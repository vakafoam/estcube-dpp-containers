# A function to get data from a database specified in the databaseConfig.py

import databaseConfig
import psycopg2

# Simple routine to run a query on a database and print the results:
def doQuery(command) :
    try:
        connection = psycopg2.connect(host=databaseConfig.HOST, user=databaseConfig.USER,
                                      password=databaseConfig.PASS, dbname=databaseConfig.DATABASE)
        cur = connection.cursor()
        cur.execute(command)
        return (cur.fetchall())
    except:
        print ("Connection to the database failed")
    finally:
        connection.close()
