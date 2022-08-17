from tkinter import *

mprin=Tk()
mprin.config(width=800,height=600)

barramenu=Menu(mprin)
mprin.config(menu=barramenu)

adminmenu=Menu(barramenu,tearoff=0)
adminmenu.add_command(label="Ingreso")
usuarios=Menu(adminmenu,tearoff=0)
usuarios.add_command(label="Crear usuario")
usuarios.add_command(label="Editar usuario")
usuarios.add_command(label="Borrar usuario")
adminmenu.add_cascade(label="Usuarios",menu=usuarios)
adminmenu.add_command(label="Configuración")



menuprod = Menu(barramenu, tearoff=0)
menuprod.add_command(label="Nuevo producto")
menuprod.add_command(label="Editar producto")
menuprod.add_command(label="Borrar producto")


factmenu = Menu(barramenu, tearoff=0)



reportmenu = Menu(barramenu, tearoff=0)


salir=Menu(barramenu,tearoff=0)
salir.add_command(label="Salir",command=mprin.quit)



barramenu.add_cascade(label="Administracion", menu=adminmenu)
barramenu.add_cascade(label="Productos", menu=menuprod)
barramenu.add_cascade(label="Facturación", menu=factmenu)
barramenu.add_cascade(label="Reportes", menu=reportmenu)
barramenu.add_cascade(label="Salir", menu=salir)








mprin.mainloop()