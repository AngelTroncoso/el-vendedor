#solicitar al usuario el precio del articulo
precio_articulo = float(input("Ingrese el precio del articulo: "))
#solicitar la cantidad de articulos
cantidad_articulos = int(input("Ingrese la cantidad de articulos: "))
#solicitar el porcentage de descuento
porcentage_descuento = float(input("Ingrese el porcentage de descuento: "))
#calcular el total a pagar con descuento
descuento= precio_articulo*(porcentage_descuento/100)
total_pagar=(precio_articulo-descuento)*cantidad_articulos
#mostrar el resultado
print(f"El Total a pagar es de : {total_pagar:.2f}Pesos")