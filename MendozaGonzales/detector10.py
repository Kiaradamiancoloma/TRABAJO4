#PROGRAMA10_CALCULAR EL TOTAL DE LA UTILIDAD PERDIDA
#DECLARACION
utilidadCPOs2005,utilidadCPOs2006,utilidadCPOs2007,utilidadCPOs2008,utilidadCPOs2009,utilidadCPOs2010=0.0,0.0,0.0,0.0,0.0,0.0
suma_utilidadper=0.0

#INPUT
utilidadCPOs2005=float(input("Ingrese el total de utilidades por perdida del año 2005: "))
utilidadCPOs2006=float(input("Ingrese el total de utilidades por perdida del año 2006: "))
utilidadCPOs2007=float(input("Ingrese el total de utilidades por perdida del año 2007: "))
utilidadCPOs2008=float(input("Ingrese el total de utilidades por perdida del año 2008: "))
utilidadCPOs2009=float(input("Ingrese el total de utilidades por perdida del año 2009: "))
utilidadCPOs2010=float(input("Ingrese el total de utilidades por perdida del año 2010: "))

#PROCESSING
suma_utilidadper=utilidadCPOs2005+utilidadCPOs2006+utilidadCPOs2007+utilidadCPOs2008+utilidadCPOs2009+utilidadCPOs2010

#Detector
#Si la suma total de utilidades es > a 1% entonces la empresa esta en perdidas
perdida_empresa=(suma_utilidadper>1)

#OUTPUT
print("#######################################")
print("#      UTILIDADES PERDIDAS EN LOS 5 AÑOS     #")
print("#######################################")
print("# utilidadCPOs2005: ",utilidadCPOs2005," #")
print("# utilidadCPOs2006: ",utilidadCPOs2006," #")
print("# utilidadCPOs2007: ",utilidadCPOs2007," #")
print("# utilidadCPOs2008: ",utilidadCPOs2008," #")
print("# utilidadCPOs2009: ",utilidadCPOs2009," #")
print("# utilidadCPOs2010: ",utilidadCPOs2010," #")
print("# Total de Utilidad P.: ",suma_utilidadper," #")
print("# PERDIDA DE LA EMPRESA: ",perdida_empresa," #")
print("#######################################")
