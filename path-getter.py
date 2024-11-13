import pathlib
import os
import platform
import sys
from pathlib import Path

class Path_getter():
    def __init__(self):
        if platform.system() == 'Windows':
            self.path = Path.cwd()
        else:
            self.path = os.getcwd()

    def get_path_directory(self, carpeta):
        #obtener el path del archivo 
        if platform.system() == 'Windows':
            nuevoPath = self.path + "\\" + carpeta + "\\"
            return nuevoPath
        else:
            nuevoPath = self.path + "/" + carpeta + "/"
            return nuevoPath
    
    def get_path_archive(self, carpeta, archive):
        #obtener el path del archivo 
        if platform.system() == 'Windows':
            nuevoPath= self.path + "\\" + carpeta + "\\" + archive
            return nuevoPath
        else:
            nuevoPath = self.path + "/" + carpeta + "/" + archive
            return nuevoPath
    
pathObtenido = Path_getter()
print(pathObtenido.get_path_directory("carpetaPrueba"))

