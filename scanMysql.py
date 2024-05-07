
from readDDL import ReadDDL
from stagesController import StagesController

# Escanea todas la bases de datos del servidor
readDDL = ReadDDL()
readDDL.setDatabaseName('information_schema')
readDDL.setPathSQL('./bbddTemplate/scanMySQL.sql')
readDDL.setPathJson('./data/database/scanMySQL.json')
readDDL.readStructureTables()

# Crea un informe completo sobre todas las tablas en el servidor
stagesController = StagesController()
stagesController.setDatabaseName("sige")
stagesController.setDatabaseJson("./data/database/scanMySQL.json")
stagesController.setPathMapp("./data/mapping/scanMySQL.json")
stagesController.setPathEndSQL("./bbdd/scanMySQL.sql")
stagesController.controller()
