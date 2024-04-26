       
from connector import Connector

class ShowTables(Connector):

    def getListTable(self, database):
        mydb = self.connectorDataBase(database)
        mycursor = mydb.cursor()
        mycursor.execute("SHOW tables")
        res = []
        for x in mycursor:
            res.append(x[0])
        return res
