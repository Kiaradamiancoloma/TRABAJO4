#Programa10-calcular el costo de venta
#Declaracion
existencia_inicial=0
costo_produccion=0.0
existencia_final=0
costo_venta=0.0

#Input
existencia_inicial=int(input("ingrese existencia_inicial:"))
costo_produccion=float(input("ingrese costo_produccion:"))
existencia_final=float(input("ingrese existencia_final:"))

#Processing
costo_venta=(existencia_inicial+costo_produccion-existencia_final)

#Detector
#sea el costo de venta>1500 entonces sus utilidades aumentaran
utilidad=(costo_venta>1500)


#Output
print("#######################")
print("#      tienda         #")
print("#######################")
print("# existencia_inicial: ",existencia_inicial," #")
print("# costo_produccion: ",costo_produccion," #")
print("# existencia_final: ",existencia_final," #")
print("# costo_venta: ",costo_venta," #")
print("# utilidad: ",utilidad," #")
print("###############################################")
