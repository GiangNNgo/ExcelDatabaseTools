from openpyxl import Workbook as WB
import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

wb = WB()

## This function connects to the database and returns the 
def connectToMySQLDatabase(hostUrl, databaseName, username, newPassword):
	print("Connecting to the database...")
	try:
		myConnection = connection.MySQLConnection(user = username, password = newPassword, 
			host = hostUrl, database = databaseName)
		# Do something here
		myConnection.close()
	except mysql.connector.Error as err:
		print("Exception detected! " + str(err.errno))
		print(err)
	


