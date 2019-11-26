#Programa5-calcular el producto bruto interno
#Declaracion
consumo=0.0
inversion_efectuada=0.0
gasto_publico=0.0
exportaciones=0.0
importaciones=0.0
producto_bruto_interno=0.0

#Input
consumo=float(input("ingrese consumo:"))
inversion_efectuada=float(input("ingrese inversion_efectuada:"))
gasto_publico=float(input("ingrese gasto_publico:"))
exportaciones=float(input("ingrese exportaciones:"))
importaciones=float(input("ingrese importaciones:"))

#Processing
producto_bruto_interno=(consumo+inversion_efectuada+gasto_publico+(exportaciones-importaciones))

#Output
print("#######################")
print("#       SENTINEL      #")
print("#######################")
print("# consumo: ",consumo)
print("# inversion_efectuada: ",inversion_efectuada)
print("# gasto_publico: ",gasto_publico)
print("# exportaciones: ",exportaciones)
print("# importaciones: ",importaciones)
print("# producto_bruto_interno: ",producto_bruto_interno)
