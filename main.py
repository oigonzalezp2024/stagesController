
import sys
from stagesController import StagesController

def main()->int:
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

if __name__ == '__main__':
    sys.exit(main())
