import mysql.connector
    
class Connector:

    def __init__(self):
       self.__host=""
       self.__user=""
       self.__password=""

    def __secret(self):
       self.__host="localhost"
       self.__user="root"
       self.__password=""

    def connectorServer(self):
        self.__secret()
        mydb = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password
        )
        return mydb

    def connectorDataBase(self, database):
        self.__secret()
        mydb = mysql.connector.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = database 
        )
        return mydb