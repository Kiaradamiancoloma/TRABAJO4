#Programa2-calcular importe prestamo
#Declaracion
importe_desembolsado=0.0
tasa_efectiva_anual=0.0
cuotas_año=0
periodo_pago=0
tasa_mensual=0.0
penalidad=0.0
dias_año=0
dias_mes=0
tna=0.0
tda=0.0
tda_ajustada_plazo=0.0

#Input
importe_desembolsado=float(input("ingrese importe_desembolsado"))
tasa_efectiva_anual=float(input("ingrese tasa_efectiva_anual:"))
cuotas_año=int(input("ingrese cuotas_año:"))
periodo_pago=int(input("ingrese periodo_pago:"))
tasa_mensual=float(input("ingrese tasa_mensual:"))
penalidad=float(input("ingrese penalidad:"))
dias_año=int(input("ingrese dias_año:"))
dias_mes=int(input("ingrese dias_mes:"))

#Processing
tna=(1+tasa_efectiva_anual**1/cuotas_año-1*cuotas_año*dias_año/360)
tda=(tasa_mensual*cuotas_año)
tda_ajustada_plazo=(tda/dias_año*dias_mes)

#detector
#Si el historial del cliente es >12000 entonces puede recibir un prestamo
historial_cliente=(importe_desembolsado>12000)

#Output
print("##########################")
print("#           BCP          #")
print("##########################")
print("# importe_desembolsado: ",importe_desembolsado," #")
print("# tasa_efectiva_anual: ",tasa_efectiva_anual," #")
print("# cuotas_año: ",cuotas_año," #")
print("# periodo_pago: ",periodo_pago," #")
print("# tasa_mensual: ",tasa_mensual," #")
print("# penalidad: ",penalidad," #")
print("# dias_año: ",dias_año," #")
print("# dias_mes: ",dias_mes," #")
print("# tna: ",tna," #")
print("# tda: ",tda," #")
print("# tda_ajustada_plazo: ",tda_ajustada_plazo," #")
print("# historial_cliente: ",historial_cliente," #")
print("###################################")
