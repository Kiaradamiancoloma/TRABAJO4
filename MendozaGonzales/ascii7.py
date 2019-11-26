#PROGRAMA7_CALCULAR EL TOTAL DE RESULTADOS DE OPERACION
#DECLARACION
resultadoper2005,resultadoper2006,resultadoper2007,resultadoper2008,resultadoper2009,resultadoper2010=0.0,0.0,0.0,0.0,0.0,0.0
total_resul=0.0

#INPUT
resultadoper2005=float(input("Ingrese los resultados totales de operaciones del año 2005: "))
resultadoper2006=float(input("Ingrese los resultados totales de operaciones del año 2006: "))
resultadoper2007=float(input("Ingrese los resultados totales de operaciones del año 2007: "))
resultadoper2008=float(input("Ingrese los resultados totales de operaciones del año 2008: "))
resultadoper2009=float(input("Ingrese los resultados totales de operaciones del año 2009: "))
resultadoper2010=float(input("Ingrese los resultados totales de operaciones del año 2010: "))

#PROCESSING
total_resul=resultadoper2005+resultadoper2006+resultadoper2007+resultadoper2008+resultadoper2009+resultadoper2010


#OUTPUT
print("#######################################")
print("#       RESULTADOS TOTALES DE OPERACIONES DEL LOS 5 AÑOS    #")
print("#######################################")
print("# resultadoper2005: ",resultadoper2005," #")
print("# resultadoper2006: ",resultadoper2006," #")
print("# resultadoper2007: ",resultadoper2007," #")
print("# resultadoper2008: ",resultadoper2008," #")
print("# resultadoper2009: ",resultadoper2009," #")
print("# resultadoper2010: ",resultadoper2010," #")
print("# Total de Resultados: ",total_resul," #")
print("#######################################")
