#Programa7-calcular el importe de interes diario
#Declaracion
saldo_final_dia=0.0
tasa_interes_ahorro=0.0
dias_base_anual=0
interes_diario=0.0

#Input
saldo_final_dia=float(input("ingrese saldo_final_dia:"))
tasa_interes_ahorro=float(input("ingrese tasa_interes_ahorr:"))
dias_base_anual=int(input("ingrese dias_base_anual:"))

#Processing
interes_diario=((saldo_final_dia*tasa_interes_ahorro)/dias_base_anual)

#Detector
#si el interes diario del cliente es <0.01 entonces sus cuotas sera mas alta
cuotas=(interes_diario<0.01)


#Output
print("#################################")
print("#        Banco Interbank        #")
print("#################################")
print("# saldo_final_dia: ",saldo_final_dia," #")
print("# tasa_interes_ahorro: ",tasa_interes_ahorro," #")
print("# dias_base_anual: ",dias_base_anual," #")
print("# interes_diario: ",interes_diario," #")
print("# cuotas:",cuotas," #")
print("########################################")
