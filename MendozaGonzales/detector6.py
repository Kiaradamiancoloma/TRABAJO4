#PROGRAMA6_CALCULAR EL PORCENTAJE TOTAL DEL MARGEN DE OPERACION
#DECLARACION
margenope2005,margenope2006,margenope2007,margenope2008,margenope2009,margenope2010=0.0,0.0,0.0,0.0,0.0,0.0
porcentajetotal2=0.0

#INPUT
margenope2005=float(input("Ingrese el margen de operacion del año 2005: "))
margenope2006=float(input("Ingrese el margen de operacion del año 2006: "))
margenope2007=float(input("Ingrese el margen de operacion del año 2007: "))
margenope2008=float(input("Ingrese el margen de operacion del año 2008: "))
margenope2009=float(input("Ingrese el margen de operacion del año 2009: "))
margenope2010=float(input("Ingrese el margen de operacion del año 2010: "))

#PROCESSING
porcentajetotal2=(margenope2005+margenope2006+margenope2007+margenope2008+margenope2009+margenope2010)*100

#Detector
#Si el porcentaje del margen de operacion es >100 entonces sus ingresos son menores
ingresos=(porcentajetotal2>100)

#OUTPUT
print("#######################################")
print("#       MARGEN DE OPERACIONES DEL LOS 5 AÑOS    #")
print("#######################################")
print("# margenope2005: ",margenope2005," #")
print("# margenope2006: ",margenope2006," #")
print("# margenope2007: ",margenope2007," #")
print("# margenope2008: ",margenope2008," #")
print("# margenope2009: ",margenope2009," #")
print("# margenope2010: ",margenope2010," #")
print("# Porcentaje Total: ",porcentajetotal2," #")
print("# Ingresos porcentaje: ",ingresos," #")
print("#######################################")
