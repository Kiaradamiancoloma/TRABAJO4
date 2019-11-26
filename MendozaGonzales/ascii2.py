#PROGRAMA2_CALCULAR LA SUMA TOTAL DE VENTAS NETAS
#DECLARACION
venetas2005,venetas2006,venetas2007,venetas2008,venetas2009,venetas2010=0,0,0,0,0,0
total_venetas=0

#INPUT
venetas2005=int(input("Ingrese el total de ventas netas del año 2005: "))
venetas2006=int(input("Ingrese el total de ventas netas del año 2006: "))
venetas2007=int(input("Ingrese el total de ventas netas del año 2007: "))
venetas2008=int(input("Ingrese el total de ventas netas del año 2008: "))
venetas2009=int(input("Ingrese el total de ventas netas del año 2009: "))
venetas2010=int(input("Ingrese el total de ventas netas del año 2010: "))

#PROCESSING
total_venetas=venetas2005+venetas2006+venetas2007+venetas2008+venetas2009+venetas2010


#OUTPUT
print("#######################################")
print("#       BOLETA VENTAS DE 5AÑOS  #")
print("#######################################")
print("# venetas2005: ",venetas2005," #")
print("# venetas2006: ",venetas2006," #")
print("# venetas2007: ",venetas2007," #")
print("# venetas2008: ",venetas2008," #")
print("# venetas2009: ",venetas2009," #")
print("# venetas2010: ",venetas2010," #")
print("#total_venetas: ",total_venetas," #")
print("#######################################")
