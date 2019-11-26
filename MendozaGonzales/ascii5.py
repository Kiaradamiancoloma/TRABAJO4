#PROGRAMA5_CALCULAR EL PORCENTAJE TOTAL DEL MARGEN DE FLUJO
#DECLARACION
margenflujo2005,margenflujo2006,margenflujo2007,margenflujo2008,margenflujo2009,margenflujo2010=0.0,0.0,0.0,0.0,0.0,0.0
porcentajetotal1=0.0

#INPUT
margenflujo2005=float(input("Ingrese el margen de flujo del año 2005: "))
margenflujo2006=float(input("Ingrese el margen de flujo del año 2006: "))
margenflujo2007=float(input("Ingrese el margen de flujo del año 2007: "))
margenflujo2008=float(input("Ingrese el margen de flujo del año 2008: "))
margenflujo2009=float(input("Ingrese el margen de flujo del año 2009: "))
margenflujo2010=float(input("Ingrese el margen de flujo del año 2010: "))

#PROCESSING
porcentajetotal1=(margenflujo2005+margenflujo2006+margenflujo2007+margenflujo2008+margenflujo2009+margenflujo2010)*100

#OUTPUT
print("#######################################")
print("#       MARGEN DE FLUJO DE LOS 5AÑOS   #")
print("#######################################")
print("# margen de fujo 2005: ",margenflujo2005," #")
print("# margen de fujo 2006: ",margenflujo2006," #")
print("# margen de fujo 2007: ",margenflujo2007," #")
print("# margen de fujo 2008: ",margenflujo2008," #")
print("# margen de fujo 2009: ",margenflujo2009," #")
print("# margen de fujo 2010: ",margenflujo2010," #")
print("# porcentajetotall: ",porcentajetotal1," #")
print("#######################################")
