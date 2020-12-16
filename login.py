# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:49:02 2020

@author: admi
"""


import controlador
import modelo


usuario =""
password = ""
bandera = False

usuario = input("Ingrese Usuario:")
password = input("Ingrese Password:")

valido = controlador.verificar_usuario(usuario,password)


if(valido == True):
        modelo.mostrar(1)
else:
    print("USUARIO INCORRECTO")