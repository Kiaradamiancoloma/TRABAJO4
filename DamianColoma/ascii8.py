#Programa8-calcular el mantenimiento de valor cuenta de ahorro
monto_principal=0.0
tipo_cambio_dia_anterior=0.0
cambio_dia_hoy=0.0
mantenimiento_valor_cuenta_de_ahorro=0.0

#Input
monto_principal=float(input("ingrese monto_principal:"))
tipo_cambio_dia_anterior=float(input("ingrese tipo_cambio_dia_anterior:"))
cambio_dia_hoy=float(input("ingrese cambio_dia_hoy:"))

#Processing
mantenimiento_valor_cuenta_de_ahorro=(monto_principal/tipo_cambio_dia_anterior*cambio_dia_hoy-monto_principal)

#Output
print("#######################")
print("#         BCR         #")
print("#######################")
print("# monto principal: ",monto_principal)
print("# tipo_cambio_dia_anterior: ",tipo_cambio_dia_anterior)
print("# cambio_dia_hoy: ",cambio_dia_hoy)
print("# mantenimiento_valor_cuenta_de_ahorro: ",mantenimiento_valor_cuenta_de_ahorro)
