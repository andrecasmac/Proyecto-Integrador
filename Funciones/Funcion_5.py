#Agregar productos a almacén
#André Castillo ya la apartó ingatu

def agregar_producto(producto, cantidad):
    almacen_viejo = open("almacenaje.txt", "r")
    lista_almacen = almacen_viejo.readlines()
    print(lista_almacen)
    print(lista_almacen[producto * 2])
    #almacen_nuevo = open("almacenaje.txt", "w")
    print(lista_almacen[:(producto * 2)]) #Todo antes de la linea que quiero

    print(lista_almacen[(producto * 2):]) #Todo después de la linea que quiero
    almacen_viejo.close()
    #almacen_nuevo.close()
    

#display productos
#Ejemplo_1:
print("[1] - Iphone 11")

p = int(input("¿Qué producto desea agregar? "))
#Asignación número-producto
#Ejemplo_1:
if p == 1:
    Producto = "Iphone 11"

Cantidad = int(input("¿Qué cantidad de productos desea agregar? "))

agregar_producto(p, Cantidad)