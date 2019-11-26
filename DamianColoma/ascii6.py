#Programa6-calcular el importe de interes generado
#Declaracion
capital_inicial=0.0
tiempo=0
interes_simple=0.0
importe_interes_generado=0.0

#Input
capital_inicial=float(input("ingrese capital_inicial:"))
tiempo=str(input("ingrese tiempo:"))
interes_simple=float(input("ingrese interes_capital"))

#Processing
importe_interes_generado=(capital_inicial*interes_simple*tiempo)

#Output
print("#######################")
print("#       Infocorp      #")
print("#######################")
print("# capital_inicial: ",capital_inicial)
print("# tiempo: ",tiempo)
print("# interes_simple: ",interes_simple)
print("# importe_interes_generado: ",importe_interes_generado)
