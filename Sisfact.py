<<<<<<< HEAD
import pandas as pd


class prod:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
asd

prod1 = prod("001", "mercedes-benz", "1", "$10.000")

def menu():
    print("1.Ingresar producto")
    print("2.Editar producto")
    print("3.Eliminar producto")
    print("4.Ventas")
    print("5.Reporte")
    option=input("Elija una opción:")
    if option == "1":
        ingprod()
    elif option == "2":
        edprod()
    elif option == "3":
        delprod()
    elif option == "4":
        sellprod()
    elif option == "5":
        repinv()
    else:
        print("No has elegido una opción correcta")
        menu()
    

def ingprod():
    print("hola")
    

def edprod():
    print("hola")

def delprod():
    print("hola")

def sellprod():
    print("hola")

def repinv():
    print("hola")


=======
import pandas as pd


class prod:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


prod1 = prod("001", "mercedes-benz", "1", "$10.000")

def menu():
    print("1.Ingresar producto")
    print("2.Editar producto")
    print("3.Eliminar producto")
    print("4.Ventas")
    print("5.Reporte")
    option=input("Elija una opción:")
    if option == "1":
        ingprod()
    elif option == "2":
        edprod()
    elif option == "3":
        delprod()
    elif option == "4":
        sellprod()
    elif option == "5":
        repinv()
    else:
        print("No has elegido una opción correcta")
        menu()
    

def ingprod():
    print("hola")
    

def edprod():
    print("hola")

def delprod():
    print("hola")

def sellprod():
    print("hola")

def repinv():
    print("hola")


>>>>>>> ee8886385d42ed30ca4e512814a40e43e1e4c8a8
