       
import json
import os
import mysql.connector
from connector import Connector

class CreateDDL(Connector):

    def setPathContent(self, pathContent):
        self.pathContent = pathContent

    def setPathMapping(self):
        self.pathContent = self.pathMapping

    def setPathBbddTemplate(self):
        self.pathContent = self.bbddTemplate

    def setPathSQL(self):
        self.pathContent = self.pathSQL

    def setContent(self):
        self.content = self.res

    def getContent(self):
        f = open(self.pathContent,"r")
        content = f.read()
        f.close()
        self.content = content

    def setTable(self):
        self.database = "./data/database/promediosSipsaCiudad.json"
        self.pathMapping = "./data/mapping/promediosSipsaCiudad.json"
        self.bbddTemplate = "./bbddTemplate/ddl.sql"
        self.databaseName = "sige"
        self.pathSQL = "./bbdd/ddl.sql"

    def getKeyNames(self):
        res = self.res
        keyNames = []
        for i in res[0]["fieldsTypes"].keys():
            keyNames.append(i)
        self.keyNames = keyNames
    
    def setPathNewMapping(self):
        self.pathJson = self.database
        self.pathContent = self.database

    def jsonLoads(self):
        self.res = json.loads(self.content)

    def defineTableStructure(self):
        ii = 0
        self.mappingCont = "" 
        for i in self.keyNames:
            fieldName = str(i)
            fieldType = str(self.res[0]["fieldsTypes"][i])
            if(fieldType != "int"):
                fieldType = "varchar"
            self.mappingCont +=fieldName+str(" ")+fieldType+str("(")+str(self.res[0]["fieldsLong"][i])+str("), ")
            ii=ii+1

    def formatContent(self):
        keyNames = self.keyNames
        self.mappingCont1 = self.content.replace("tableName", self.res[0]["tableName"])
        contentA = self.mappingCont1.replace("()","("+str(self.mappingCont[:-2])+")")
        res = contentA.replace(", ",",\n").replace("))",")\n)").replace(keyNames[0],"\n"+str(keyNames[0]))
        self.res = res+str(";\n\n")

    def updateContent(self):
        f = open(self.pathContent,"w")
        f.write(self.content)
        f.close()

    def newContent(self):
        f = open(self.pathContent,"w")
        f.write(self.content)
        f.close()

    def createTable(self):
        database = self.databaseName
        pathSQL = self.pathSQL
        mydb = self.connectorDataBase(database)
        mycursor = mydb.cursor()
        f = open(pathSQL,"r")
        content = f.read()
        f.close()
        mycursor.execute(content)

    def getMappingKeyNames(self):
        self.keyNames = []
        for i in self.res[0].keys():
            self.keyNames.append(i)

    def mapping(self):
        self.mappingN = {}
        self.dataT = []
        self.longgN = {}
        self.typesN = {}
        for i in self.keyNames:
            self.mappingN[i] = []
            
        self.stage1()
        self.stage2()
        self.stage3()
        self.stage4()
        self.stage5()
        self.stage6()

    def stage1(self):
        for i in self.res:
            for ii in self.keyNames:
                self.mappingN[ii].append(i[ii])

    def stage2(self):
        for keyy in self.mappingN:
            self.dataT.append(self.mappingN[keyy])

    def stage3(self):
        i = 0
        for ii in self.mappingN:
            self.typesN[ii] = str(type(self.dataT[i][0])).replace("<class '","").replace("\'>","")
            self.longgN[ii] = len(str(max(self.dataT[i])))
            i = i+1

    def stage4(self):
        self.databaseNameN = self.database.replace(os.path.split(self.database)[1], "").replace("./data/","").replace("/","")
        self.tableNameN = os.path.split(self.database)[1].replace(".json","")
        self.dataN = self.res[0]

    def stage5(self):
        self.mappingN = []
        self.mappingN.append({
            "databaseName": self.databaseNameN,
            "tableName": self.tableNameN,
            "fieldsTypes": self.typesN,
            "fieldsLong": self.longgN,
            "example": self.dataN
        })

    def stage6(self):
        self.content = json.dumps(self.mappingN, sort_keys=False, indent=4)
        self.pathContent = "./data/mapping/"+str(self.tableNameN)+str(".json")

    def insertMigr(self):
        database = self.databaseName
        mydb = self.connectorDataBase(database)
        mycursor = mydb.cursor()
        text = ""
        bind = "%s,"
        binds = ""
        for i in self.keyNames:
            text = text+str(i)+", "
            binds = binds+bind

        sql = "INSERT INTO "+str(self.tableNameN)+"("+str(text[:-2])+") VALUES ("+str(binds[:-1])+");"
        f = open("./data/database/"+str(self.tableNameN)+".json","r")
        content = f.read()
        f.close()

        res = json.loads(content)
        print("Registros a cargar",len(res))
        keys = []
        for i in res[0]:
            keys.append(i)
        data = []
        for ii in res:
            regg = []
            cont = 0
            for i in ii:
                key = keys[cont]
                regg.append(ii[key])
                cont = cont+1
            data.append(regg)

        n = 100
        output = [data[i : i + n] for i in range(0, len(data), n)]

        for i in output:
            mycursor.executemany(sql, i)
            mydb.commit()
        print(mycursor.rowcount, "was inserted.")
