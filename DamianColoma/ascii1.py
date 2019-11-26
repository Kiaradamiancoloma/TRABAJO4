#Programa1-calcular el promedio de deuda de un cliente
#Declaracion
deuda_bcp=0.0
deuda_bbva=0.0
deuda_cajas=0.0
deuda_otras=0.0
deuda_promedio=0.0

#Input
deuda_bcp=float(input("ingrese deuda_bcp:"))
deuda_bbva=float(input("ingrese deuda_bbva:"))
deuda_cajas=float(input("ingrese deuda_cajas:"))
deuda_otras=float(input("ingrese deuda_otras:"))

#Processing
deuda_promedio=((deuda_bcp+deuda_bbva+deuda_cajas+deuda_otras)/4)

#Output
print("#######################")
print("#       Infocorp      #")
print("#######################")
print("# deuda_bcp: ",deuda_bcp)
print("# deuda_bbva: ",deuda_bbva)
print("# deuda_cajas: ",deuda_cajas)
print("# deuda_otras: ",deuda_otras)
print("# deuda_promedio: ",deuda_promedio)



















