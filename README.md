
# StagesController 

## ¿Qué hace StagesController?
La clase StagesController permite:

- Establece la configuración DDL mínina de una tabla de base de una datos MySQL destino, a partir de una estructura Json que se haya generado a partir de la consulta a una base de datos origen.
- Crea el diseño de las tablas necesarias para el diseño de la base de datos destino en:<b>"./bbdd/ddl.sql"</b>.
- Después de establecer la configuración de las tablas, crea las tablas en la base de datos destino y ejecuta las consultas desarrolladas por el mismo, todo de forma automática.  

Desde luego, esta es una herramienta para usar solo en entornos de desarrollo.

## En etapa de desarrollo:
La próxima mejora:
- Que el programa poble la tabla de la base de datos destino, a partir del diseño de una consulta que el mismo haya configurado, terminando así un proceso de integración básico.

## Documentación técnica

### Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |

### Librerías del proyecto.
| librería | Descripción | Comando |
| :----    | :---        | :---    |
| mysql-connector | Permite el acceso a una base de datos mysql | python -m pip install mysql-connector |

### Realice sus pruebas, actualizaciones o modificaciones.
> Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.

> Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```

---

#### Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Realice pruebas de rutina.                    | py main.py |
| Paso 8 | Finalice su gestión.                          | deactivate                            |

