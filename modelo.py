# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:49:25 2020

@author: admi
"""


#import sqlite3

import conexion


def Principal():
    print("\t \t \t \n\n\n\t\t MENU:" +
      "\n 1 - Listar"+
      "\n 2 - Agregar"+
      "\n 3 - Eliminar"+
      "\n 4 - Modificar"+
      "\n 5 - Salir ")



def Agregar():
    pro_name = input("Ingrese nombre del producto:")
    pro_codigo =input("Ingrese codigo del producto:")    
    pro_precio =input("Ingrese precio del producto:")
    
    sql_agregar = f"insert into producto (nombre,codigo,precio) VALUES('{pro_name}','{pro_codigo}','{pro_precio}')"                 
    conexion.cursor.execute(sql_agregar)
    conexion.conexion.commit()
    
def listar():
    sql_select_producto = "select * from PRODUCTO"
    conexion.cursor.execute(sql_select_producto)
    array_producto = conexion.cursor.fetchall()
    print(f"ID\t"+f"NOMBRE\t\t"+f"CODIGO\t"+f"PRECIO")
    for producto in array_producto: 
        print(f"{producto[0]}\t"+f"{producto[1]}\t\t"+f"{producto[2]}\t"+f"{producto[3]}")
        
    
def Eliminar():
    listar()
    idpro = input("Ingrese el CODIGO del producto a ELIMINAR:")
    selec_id = f"select CODIGO from PRODUCTO WHERE CODIGO='{idpro}'"
    conexion.cursor.execute(selec_id)
    array_id_pro = conexion.cursor.fetchall()

    if(len(array_id_pro)>0):
        sql_eliminar =f"delete from PRODUCTO WHERE CODIGO ='{idpro}'"
        conexion.cursor.execute(sql_eliminar)
        conexion.conexion.commit()
    else:
        print("CODIGO del Producto no encontrado")
    
    
def Mofificar():
    listar()
    idpro = input("Ingrese el CODIGO del producto a MODIFICAR:")
    selec_id = f"select codigo from producto WHERE codigo='{idpro}'"
    conexion.cursor.execute(selec_id)
    array_id_pro = conexion.cursor.fetchall()
    
    if(len(array_id_pro)>0):
        nombre_pro = input("Ingrese El NUEVO NOMBRE DEL PRODUCTO:")
        precio_pro = input("Ingrse El NUEVO PRECIO:")
        sql_modificar=f"update PRODUCTO set NOMBRE='{nombre_pro}', PRECIO='{precio_pro}'  WHERE CODIGO ='{idpro}'"
        conexion.cursor.execute(sql_modificar)
        conexion.conexion.commit()
    else:
        print("CODIGO del Producto no encontrado")   

    
def salir():
    exit()
  
   
def error():
   print("Digito No valido")


bandera =""
menu_o=1

def mostrar(menu_o):
  
    while(menu_o != 5):
         Principal()
         menu_o = int(input("Ingrese Operacion:"))
         if(menu_o == 1):
             listar()
         elif(menu_o == 2):
             Agregar()
         elif(menu_o == 3):
             Eliminar()
         elif(menu_o == 4):
             Mofificar()
         elif(menu_o==5):
             print("********* Sesion Finalizada ********")
         else:  error()
               
   
       

