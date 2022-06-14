import pandas as pd




def ingprod():
    menuingpro=["Introduzca el codigo del producto: ","Introduzca el nombre del producto: ","Introduzca la cantidad del producto: ","Introduzca el precio del producto: "]
    nprod=[]
    for i in range(4):
        dato=input(menuingpro[0])
        nprod.append(dato)
        menuingpro.pop(0)
    print("Nuevo producto creado\nCodigo: ",nprod[0],"\nNombre: ",nprod[1],"\nCantidad: ",nprod[2],"\nPrecio: ",nprod[3])

opcion=0

while opcion != 4:
    print("1.Ingresar producto\n2.Editar producto\n3.Eliminar producto\n4.Ventas\n5.Reporte\n6.Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion==1:
        ingprod()
    elif opcion==2:
        editprod()
    elif opcion==3:
        elimprod()
    elif opcion==4:
        ventas()
    elif opcion==5:
        reporte()
    elif opcion==6:
        print("Saliendo")
    else:
        print("Ingrese una opción valida")
    


