## This example uses mysql-connector and openpyxl to fetch data from a database 
## and write it into an excel file.
## Real applications will depend on the actual database's structures.

from openpyxl import Workbook as WB
import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

wb = WB()

## This function connects to the database and returns the cursor
def connectToMySQLDatabase(hostUrl, databaseName, username, newPassword, newQuery):
	print("Connecting to the database...")
	try:
		# First, connect to the database
		myConnection = connection.MySQLConnection(user = username, password = newPassword, 
			host = hostUrl, database = databaseName)
		# Execute the query here
		myConnection.close()
	except mysql.connector.Error as err:
		print("Exception detected! " + str(err.errno))
		print(err)
	
def main():
	print "Hello World!"

if __name__== "__main__":
	main()