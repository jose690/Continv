import pandas as pd
import os

def ingprod():
    while True:
        agregar_producto=input('Desea agregar un producto S/N ')
        if (agregar_producto=='S')|(agregar_producto=='s'):
            valcodigo=input('CODIGO ')
            valnombre=input('NOMBRE ')
            valcantidad=input('CANTIDAD ')
            valprecio=input('PRECIO ')

            p={'CODIGO':[int(valcodigo)],'NOMBRE':[str(valnombre)],'CANTIDAD':[int(valcantidad)],'PRECIO':[int(valprecio)]}
            df=pd.DataFrame(p)
            df.to_csv('datos.csv',mode='a',index=False,header=False)
            print('Datos agregados satisfactoriamente')

        else:
            break

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elija una opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

salir=False
option=0
while not salir:

    print("1.Ingresar producto")
    print("2.Editar producto")
    print("3.Eliminar producto")
    print("4.Ventas")
    print("5.Reporte")
    print('6.Salir')
    option = pedirNumeroEntero()
    if option == 1:
        ingprod()
    elif option == 2:
        edprod()
    elif option == 3:
        delprod()
    elif option == 4:
        sellprod()
    elif option == 5:
        repinv()
    elif option==6:
        salir=True
    else:
        print ("Introduce un numero entre 1 y 5")

        



    
