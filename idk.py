from cgitb import text
from mimetypes import init
from openpyxl import *
import mysql.connector
from tkinter import *
import tkinter as tk

conexion=mysql.connector.connect(host="localhost",database="proyectosupermercado",user="root",password="Jfgch5673")
cursornombre=conexion.cursor()
name=("SELECT Nombre FROM producto")
cursornombre.execute(name)
for i in cursornombre:
    maxe=i
    

class producto:
    def __init__(self,idproducto,Nombre,Cantidad,Precio,idMarca,idCategoria,idProveedor):
        self.idproducto=idproducto
        self.nombre=Nombre
        self.cantidad=Cantidad
        self.precio=Precio
        self.marca=idMarca
        self.categoria=idCategoria
        self.proveedor=idProveedor
        

interfaz=Tk()
interfaz.geometry("1200x600")
interfaz.title("Productos")
nombre=Label(interfaz,text="Nombre")
valnombre=Text(interfaz,width=30,height=10)
valnombre.insert(END,maxe)
nombre.grid(row=0,column=0)
valnombre.grid(row=1,column=0)


interfaz.mainloop()


