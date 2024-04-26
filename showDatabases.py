       
from connector import Connector

class ShowDatabases(Connector):

    def getListDataBases(self):
        mydb = self.connectorServer()
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        res = []
        for x in mycursor:
            res.append(x[0])
        return res
