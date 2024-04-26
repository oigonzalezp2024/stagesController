
from createDDL import CreateDDL

class StagesController(CreateDDL):

    def setDatabaseName(self, databaseName):
        self.databaseName = databaseName

    def setBbddTemplate(self, bbddTemplate):
        self.bbddTemplate = bbddTemplate

    def setPathEndSQL(self, pathSQL):
        self.pathSQL = pathSQL

    def setDatabaseJson(self, database):
        self.database = database

    def setPathMapp(self, pathMapping):
        self.pathMapping = pathMapping

    def controller(self):
        self.setPathNewMapping()
        self.getContent()
        self.jsonLoads()  
        self.getMappingKeyNames()
        self.mapping()
        self.newContent()
        self.setPathMapping()
        self.getContent()
        self.jsonLoads()
        self.setPathBbddTemplate()
        self.getContent()
        self.getKeyNames()
        self.defineTableStructure()
        self.setPathSQL()
        self.formatContent()
        self.setContent()
        self.updateContent()
        self.createTable()
        self.insertMigr()