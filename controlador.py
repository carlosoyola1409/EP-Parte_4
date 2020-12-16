# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:49:39 2020

@author: admi
"""


import sqlite3
import conexion


def verificar_usuario(usuario,password):
    
    sql_autentificar = "select * from usuario"
    conexion.cursor.execute(sql_autentificar)
    array_usuarios=conexion.cursor.fetchall()
    for user in array_usuarios:
        if(user[1] == usuario and user[2]==password):
            print("***********Sesion Iniciada******")
            return True
        else:
            #print("error de autentificacion");
            return False
