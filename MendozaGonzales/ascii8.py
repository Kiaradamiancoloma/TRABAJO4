#PROGRAMA8_CALCULAR EL TOTAL DE LA PARTICIPACION NO CONTROLADA
#DECLARACION
partnocontr2005,partnocontr2006,partnocontr2007,partnocontr2008,partnocontr2009,partnocontr2010=0,0,0,0,0,0
total_partno=0

#INPUT
partnocontr2005=int(input("Ingrese el total de participacion no controlada del año 2005: "))
partnocontr2006=int(input("Ingrese el total de participacion no controlada del año 2006: "))
partnocontr2007=int(input("Ingrese el total de participacion no controlada del año 2007: "))
partnocontr2008=int(input("Ingrese el total de participacion no controlada del año 2008: "))
partnocontr2009=int(input("Ingrese el total de participacion no controlada del año 2009: "))
partnocontr2010=int(input("Ingrese el total de participacion no controlada del año 2010: "))

#PROCESSING
total_partno=partnocontr2005+partnocontr2006+partnocontr2007+partnocontr2008+partnocontr2009+partnocontr2010

#OUTPUT
print("#######################################")
print("#      Participaciones No Controladas     #")
print("#######################################")
print("# partnocontr2005: ",partnocontr2005," #")
print("# partnocontr2006: ",partnocontr2006," #")
print("# partnocontr2007: ",partnocontr2007," #")
print("# partnocontr2008: ",partnocontr2008," #")
print("# partnocontr2009: ",partnocontr2009," #")
print("# partnocontr2010: ",partnocontr2010," #")
print("# Total de Participaciones: ",total_partno," #")
print("#######################################")
