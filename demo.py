
from stagesController import StagesController

stagesController = StagesController()
stagesController.setDatabaseName("sige")
stagesController.setBbddTemplate("./bbddTemplate/ddl.sql")

stagesController.setPathEndSQL("./bbdd/customers.sql")
stagesController.setDatabaseJson("./data/database/customers.json")
stagesController.setPathMapp("./data/mapping/customers.json")
stagesController.controller()

stagesController.setPathEndSQL("./bbdd/promediosSipsaCiudad.sql")
stagesController.setDatabaseJson("./data/database/promediosSipsaCiudad.json")
stagesController.setPathMapp("./data/mapping/promediosSipsaCiudad.json")
stagesController.controller()
