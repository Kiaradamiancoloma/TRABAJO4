#PROGRAMA1_CALCULAR LA SUMA TOTAL DE VENTAS DEL 2013 DE LOS PRIMEROS 6 MESES
#DECLARACION
ventas_enero2013, ventas_febrero2013, ventas_marzo2013, ventas_abril2013, ventas_mayo2013, ventas_junio2013=0.0,0.0,0.0,0.0,0.0,0.0
total_ventas2013=0.0

#INPUT
ventas_enero2013=float(input("Ingrese el total de ventas del mes de enero: "))
ventas_febrero2013=float(input("Ingrese el total de ventas del mes de febrero: "))
ventas_marzo2013=float(input("Ingrese el total de ventas del mes de marzo: "))
ventas_abril2013=float(input("Ingrese el total de ventas del mes de abril:"))
ventas_mayo2013=float(input("Ingrese el total de ventas del mes de mayo:"))
ventas_junio2013=float(input("Ingrese el total de ventas del mes de abril:"))

#PROCESSING
total_ventas2013=ventas_enero2013+ventas_febrero2013+ventas_marzo2013+ventas_abril2013+ventas_mayo2013+ventas_junio2013

#Detector
#la suma del total de ventas es < 10000 entonces hay mas ganancias
ganancias_ventas=(total_ventas2013<10000)

#OUTPUT
print("#######################################")
print("#       BOLETA VENTAS 2013   #")
print("#######################################")
print("# ventas_enero2013: ",ventas_enero2013," #")
print("# ventas_febrero2013: ",ventas_febrero2013," #")
print("# ventas_marzo2013: ",ventas_marzo2013," #")
print("# ventas_abril2013: ",ventas_abril2013," #")
print("# ventas_mayo2013: ",ventas_mayo2013," #")
print("# ventas_junio2013:",ventas_junio2013," #")
print("#total_ventas2013:",total_ventas2013," #")
print("# ganancias_ventas: ",ganancias_ventas," #")
print("#######################################")



























