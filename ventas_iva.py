# Determine las ventas con iva para n ventas


sw = True #inicia "bandera"
x = 1 #contador 
while sw == True:
    respuesta = input("Desea saber el valor de un producto con iva? s/n \n")
    respuesta = respuesta.upper()
    if respuesta == "S":
        producto = int(input(f"Ingrese el valor del producto {x} $"))
        precio_con_iva = producto*1.19
        print(f"Precio con iva ${precio_con_iva}")
        x+=1
    elif respuesta == "N":
        print("Adiosito")
        sw = False
    else:
        print("Ingrese S o N !!")

