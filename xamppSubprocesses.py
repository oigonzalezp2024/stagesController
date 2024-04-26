
import subprocess

class XammpSubprocesses:

    def __init__(self):
        self.__secret()
        self.xamppControl()
        self.apacheStart()
        self.mysqlStart()

    def __secret(self):
        self.__pathControl = "C:/xampp/xampp-control.exe"
        self.__pathApacheStart = "/xampp/apache_start.bat"
        self.__pathMysqlStart = "/xampp/mysql_start.bat"

    def xamppControl(self):
        self.__secret()
        subprocess.Popen(self.__pathControl)
        
    def apacheStart(self):
        subprocess.Popen(self.__pathApacheStart)
        
    def mysqlStart(self):
        subprocess.Popen(self.__pathMysqlStart)
