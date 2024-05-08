       
import json
from connector import Connector

class ReadDDL(Connector):

    def setDatabaseName(self, databaseName:str)->None:
        self.__databaseName = str(databaseName)

    def getDatabaseName(self)->str:
        return self.__databaseName

    def setPathSQL(self, pathSQL:str)->None:
        self.__pathSQL = str(pathSQL)

    def getPathSQL(self)->str:
        return self.__pathSQL

    def setPathJson(self, pathJson:str)->None:
        self.__pathJson = str(pathJson)

    def getPathJson(self)->str:
        return self.__pathJson
    
    def readFile(self, path):
        f = open(path,"r")
        content = f.read()
        f.close()
        return content
    
    def writeFile(self, path, data):
        f = open(path,"w")
        f.write(json.dumps(data, indent=4, sort_keys=False))
        f.close()

    def readStructureTables(self):
        mydb = self.connectorDataBase(self.getDatabaseName())
        mycursor = mydb.cursor()
        content = self.readFile(self.getPathSQL())
        content = content.replace('/n',' ')
        mycursor.execute(content)
        res = mycursor.fetchall()

        data = []
        for i in res:
            self.setConfigDatabase(i)
            reg = self.getConfigDatabase()
            data.append(reg)
        self.writeFile(self.getPathJson(), data)

    def setConfigDatabase(self, i):
        cont = 0
        data = []
        for y in i:
            if (len(str(y))<=0 or y==None):
                data.append("-")
            else:
                data.append(y)
            cont+=int(1)

        i = data
        self.table_schema = i[0]
        self.table_name = i[1]
        self.ordinal_position = i[2]
        self.column_name = i[3]
        self.data_type = i[4]
        self.data_length = i[5]
        self.column_key = i[6]
        self.ref_col_name = i[7]
        self.ref_name = i[8]

    def getConfigDatabase(self):
        reg = {
            'table_schema':self.table_schema,
            'table_name':self.table_name,
            'ordinal_position':self.ordinal_position,
            'column_name':self.column_name,
            'data_type':self.data_type,
            'data_length':self.data_length,
            'column_key':self.column_key,
            'ref_col_name':self.ref_col_name,
            'ref_name':self.ref_name
        }
        return reg
