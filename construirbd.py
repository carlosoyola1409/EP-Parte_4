# -*- coding: utf-8 -*-
import sqlite3

archivo1 = open("usuarios.txt","rt", encoding = 'utf8')
archivo2 = open("claves.txt","rt", encoding = 'utf8')
archivo3 = open("nombre.txt","rt", encoding = 'utf8')
archivo4 = open("codigo.txt","rt", encoding = 'utf8')
archivo5 = open("precio.txt", "rt", encoding = 'utf8')
datos_archivo1 = archivo1.read()
datos_archivo2= archivo2.read()
datos_archivo3 = archivo3.read()
datos_archivo4 = archivo4.read()
datos_archivo5 = archivo5.read()
lista_usuarios=datos_archivo1.split()
lista_claves=datos_archivo2.split()
lista_nombre=datos_archivo3.split()
lista_codigo=datos_archivo4.split()
lista_precio=datos_archivo5.split()
lista_users=[]
lista_productos=[]
union1=zip(lista_usuarios, lista_claves)
union2=zip(lista_nombre,lista_codigo,lista_precio)
lista_users=list(union1)
lista_productos=list(union2)


conexion = sqlite3.connect("ventas.db")
tabla_usuario = """CREATE TABLE usuario(
                        idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT,
                        clave TEXT
                        )
                """
tabla_producto ="""CREATE TABLE producto(
                        idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        codigo TEXT,
                        precio REAL
                        )
                """
insert_usuario=""" INSERT INTO USUARIO(USUARIO,CLAVE)
                    VALUES(?,?) """
insert_producto=""" INSERT INTO PRODUCTO(NOMBRE,CODIGO,PRECIO)
                    VALUES(?,?,?)"""
                    
cursor = conexion.cursor()
cursor.execute(tabla_usuario)
cursor.execute(tabla_producto)
cursor.executemany(insert_usuario,lista_users)
cursor.executemany(insert_producto, lista_productos)
conexion.commit()
conexion.close()
archivo1.close()
archivo2.close()
archivo3.close()
archivo4.close()
archivo5.close()