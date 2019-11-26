#Programa4-calcular el promedio de deuda de un cliente
#Declaracion
tasa_de_interes=0.0
capital_prestamo=0.0
plazo_num_cuotas=0
cuota=0.0

#Input
tasa_de_interes=float(input("ingrese tasa_de_interes:"))
capital_prestamo=float(input("ingrese capital_prestamo:"))
plazo_num_cuotas=int(input("ingrese plazo_num_cuotas:"))

#Processing
cuota=(capital_prestamo*(1+tasa_de_interes**plazo_num_cuotas*tasa_de_interes/(1+tasa_de_interes)**plazo_num_cuotas)-1)

#Output
print("###############################")
print("#      Caja municipal ica     #")
print("###############################")
print("# tasa_de_interes: ",tasa_de_interes)
print("# capital_prestamo: ",capital_prestamo)
print("# plaza_num_cuotas: ",plazo_num_cuotas)
print("# cuota: ",cuota)
