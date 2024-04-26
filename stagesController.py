
from createDDL import CreateDDL

class StagesController(CreateDDL):

    def controller(self):
        self.xammpSubprocesses()
        self.setTable()
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
