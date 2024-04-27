
import sys
from stagesController import StagesController

def main()->int:
    stagesController = StagesController()
    # define el nombre de la base de datos destino
    stagesController.setDatabaseName("sige")
    
    # Primera tabla
    # estructura Json a procesar
    stagesController.setDatabaseJson("./data/database/customers.json")
    # ruta donde se guardará el mapeo
    stagesController.setPathMapp("./data/mapping/customers.json")
    # ruta donde se guardará el dll generado
    stagesController.setPathEndSQL("./bbdd/customers.sql")
    ### ejecutese el programa
    stagesController.controller()

    # Segunda tabla

    stagesController.setDatabaseJson("./data/database/promediosSipsaCiudad.json")
    stagesController.setPathMapp("./data/mapping/promediosSipsaCiudad.json")
    stagesController.setPathEndSQL("./bbdd/promediosSipsaCiudad.sql")
    stagesController.controller()

if __name__ == '__main__':
    sys.exit(main())
