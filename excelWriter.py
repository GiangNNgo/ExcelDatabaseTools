from openpyxl import Workbook as WB
import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

wb = WB()

def connectToDatabase(hostUrl, databaseName, username, newPassword):
	print("Let's connect to a database.")
	try:
		myConnection = connection.MySQLConnection(user = username, password = newPassword, 
			host = hostUrl, database = databaseName)
		myConnection.close()
	except mysql.connector.Error as err:
		print("Exception detected! " + str(err.errno))
		print(err)
	print("Well let's keep going!")


def main():
	return 0

connectToDatabase('a', 'b', 'c', 'd')