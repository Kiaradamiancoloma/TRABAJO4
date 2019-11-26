#PROGRAMA3_CALCULAR LA SUMA TOTAL DEl COSTO DE VENTAS
#DECLARACION
costoven2005,costoven2006,costoven2007,costoven2008,costoven2009,costoven2010=0,0,0,0,0,0
total_costoven=0

#INPUT
costoven2005=int(input("Ingrese el total de costos del año 2005"))
costoven2006=int(input("Ingrese el total de costos del año 2006"))
costoven2007=int(input("Ingrese el total de costos del año 2007"))
costoven2008=int(input("Ingrese el total de costos del año 2008"))
costoven2009=int(input("Ingrese el total de costos del año 2009"))
costoven2010=int(input("Ingrese el total de costos del año 2010"))

#PROCESSING
total_costoven=costoven2005+costoven2006+costoven2007+costoven2008+costoven2009+costoven2010

#OUTPUT
print("#######################################")
print("#       BOLETA DE COSTOS DE VENTAS DE 5AÑOS  #")
print("#######################################")
print("# costoven2005: ",costoven2005," #")
print("# costoven2006: ",costoven2006," #")
print("# costoven2007: ",costoven2007," #")
print("# costoven2008: ",costoven2008," #")
print("# costoven2009: ",costoven2009," #")
print("# costoven2010: ",costoven2010," #")
print("# total_costoven: ",total_costoven," #")
print("#######################################")
