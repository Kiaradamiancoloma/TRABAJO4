#PROGRAMA9_CALCULAR LA SUMA TOTAL DE DIVIDENDOS POR CPO
#DECLARACION
dividendosCPOs2005,dividendosCPOs2006,dividendosCPOs2007,dividendosCPOs2008,dividendosCPOs2009,dividendosCPOs2010=0.0,0.0,0.0,0.0,0.0,0.0
suma_dividendosCPO=0.0

#INPUT
dividendosCPOs2005=float(input("Ingreso total de dividendos por CPO en el año 2005: "))
dividendosCPOs2006=float(input("Ingreso total de dividendos por CPO en el año 2006: "))
dividendosCPOs2007=float(input("Ingreso total de dividendos por CPO en el año 2007: "))
dividendosCPOs2008=float(input("Ingreso total de dividendos por CPO en el año 2008: "))
dividendosCPOs2009=float(input("Ingreso total de dividendos por CPO en el año 2009: "))
dividendosCPOs2010=float(input("Ingreso total de dividendos por CPO en el año 2010: "))

#PROCESSING
suma_dividendosCPO=dividendosCPOs2005+dividendosCPOs2006+dividendosCPOs2007+dividendosCPOs2008+dividendosCPOs2009+dividendosCPOs2010

#OUTPUT
print("#######################################")
print("#     Dividendos por CPO en los 5 años     #")
print("#######################################")
print("# dividendosCPOs2005: ",dividendosCPOs2005," #")
print("# dividendosCPOs2006: ",dividendosCPOs2006," #")
print("# dividendosCPOs2007: ",dividendosCPOs2007," #")
print("# dividendosCPOs2008: ",dividendosCPOs2008," #")
print("# dividendosCPOs2009: ",dividendosCPOs2009," #")
print("# dividendosCPOs2010: ",dividendosCPOs2010," #")
print("# Total de dividendos: ",suma_dividendosCPO," #")
print("#######################################")
