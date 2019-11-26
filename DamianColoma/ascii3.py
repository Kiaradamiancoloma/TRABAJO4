#Programa3-calcular la cuota
monto=0.0
plazo=0
tasa_efectiva_mensual=0.0
comision=0.0
seguro_desgravamen=0.0
saldo_capital=0.0
tea=0.0
ted=0.0
suma_factores=0.0
cuota=0.0

#Input
monto=float(input("ingrese monto:"))
plazo=int(input("ingrese plazo"))
tasa_mensual=float(input("ingrese tasa_mensual"))
comision=float(input("ingrese comision:"))
seguro_desgravamen=float(input("ingrese seguro_desgravamen:"))
saldo_capital=float(input("ingrese saldo_capital:"))
suma_factores=float(input("ingrese suma_factores:"))

#Processing
tea=((1+tasa_mensual)**plazo-1)
ted=(1+tea)**0.0027-1
cuota=(saldo_capital+suma_factores)

#Output
print("############################")
print("#       Banco Ripley       #")
print("############################")
print("# monto: ",monto)
print("# plazo: ",plazo)
print("# tasa_efectiva_mensual: ",tasa_mensual)
print("# seguro_desgravamen: ",seguro_desgravamen)
print("# saldo_capital: ",saldo_capital)
print("# tea: ",tea)
print("# ted: ",ted)
print("# suma_factores: ",suma_factores)
print("# cuota:",cuota)
