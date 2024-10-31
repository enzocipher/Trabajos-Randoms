import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

class Miembro:
    def __init__(self) -> None:
        self.__DNI
        self.__nombre_completo
        self.__rol  #JP, DEV,QA

class Incidencia:
    def __init__(self) -> None:
        self.__id
        self.__estado  # A / P / L
        self.__tipo = "" # falla de sistema, perfonmance, usabilidad
        self.__fecha_rceacion = datetime.datetime.now()
        self.__tipo_prueba # [pruebas]
        self.__desarrollador_responsable_de_incidencia
        self.__descripcion
        self.__fecha_resolucion_qa  # datatime
        self.__fecha_reasignadcion_desarrollo
        self.__fecha_cierre
        self.__desarrollador_responsable_de_solucion

class Manejador_Incidencias:

    def __init__(self) -> None:
        self.__incidencias = {}

class Proyecto():
    def __init__(self, codigo, nombre, descripcion, nombre_jefe):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__nombre_jefe = nombre_jefe
        self.__incidencias =  Manejador_Incidencias()
        # responsable_prueba_qa: incidencia
        self.__tipo_proyecto
        self.__miembros_proyecto = []


    def registar_miembro(self):
        self.__miembros_proyecto.append(Miembro())

    def registrar_indicencia(self):
        pass




