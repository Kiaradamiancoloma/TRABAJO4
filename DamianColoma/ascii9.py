#Programa9-calcular el promedio de deuda de un cliente
#Declaracion
materia_prima_directa=0.0
materia_prima_comprada=0.0
materia_prima_disponible=0.0
materia_directa_final_disponible=0.0
materia_prima_utilizada=0.0
mano_obra=0.0
costo_indirecto=0.0
producto_proceso=0.0
produc_inicial=0.0
costo_produccion=0.0

#Input
materia_prima_directa=float(input("ingrese materia_prima_directa:"))
materia_prima_comprada=float(input("ingrese materia_prima_comprada:"))
materia_directa_final_disponible=float(input("ingrese materia_directa_final_disponible:"))
mano_obra=float(input("ingrese mano_obra;"))
costo_indirecto=float(input("ingrese costo_indirecto:"))
producto_proceso=float(input("ingrese producto_proceso:"))
produc_inicial=float(input("ingrese produc_inicial:"))

#Processing
materia_prima_disponible=(materia_prima_directa+materia_prima_comprada)
costo_produccion=(materia_prima_disponible+mano_obra+materia_prima_comprada-producto_proceso)

#Output
print("###############################")
print("#      Caja municipal ica     #")
print("###############################")
print("# materia_prima_directa: ",materia_prima_directa)
print("# materia_prima_comprada: ",materia_prima_comprada)
print("# materia_directa_final_disponible: ",materia_directa_final_disponible)
print("# mano_obra: ",mano_obra)
print("# materia_prima_disponible: ",materia_prima_disponible)
print("# materia_prima_utilizada: ",materia_prima_utilizada)
print("# costo_produccion: ",costo_produccion)
