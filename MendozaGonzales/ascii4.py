#PROGRAMA4_CALCULAR EL TOTAL DE LAS ESPECIES EN RIESGO
#DECLARACION
anfibios_riesgo,coniferas_riesgo,corales_riesgo,tiburones_riego,crustaceos_riesgo,mamiferos_riesgo,aves_riesgo=0,0,0,0,0,0,0
sumatotal=0

#INPUT
anfibios_riesgo=int(input("Ingrese el total de anfibios en peligro de riesgo: "))
coniferas_riesgo=int(input("Ingrese el total de coniferas en peligro de riesgo: "))
corales_riesgo=int(input("Ingrese el total de corales en peligro de riesgo: "))
tiburones_riego=int(input("Ingrese el total de tiburones en peligro de riesgo: "))
crustaceos_riesgo=int(input("Ingrese el total de crustaceos en peligro de riesgo: "))
mamiferos_riesgo=int(input("Ingrese el total de mamiferos en peligro de riesgo: "))
aves_riesgo=int(input("Ingrese el total de aves en peligro de riesgo: "))

#PROCESSING
sumatotal=anfibios_riesgo+coniferas_riesgo+corales_riesgo+tiburones_riego+crustaceos_riesgo+mamiferos_riesgo+aves_riesgo

#OUTPUT
print("#######################################")
print("#       ESPECIES EN RIESGO    #")
print("#######################################")
print("# anfibios_riesgo: ",anfibios_riesgo," #")
print("# coniferas_riesgo: ",coniferas_riesgo," #")
print("# corales_riesgo: ",corales_riesgo," #")
print("# tiburones_riesgo: ",tiburones_riego," #")
print("# crustaceos_riesg: ",crustaceos_riesgo," #")
print("# mamiferos_riesgo: ",mamiferos_riesgo," #")
print("# aves_riesgo: ",aves_riesgo," #")
print("# sumatotal: ",sumatotal," #")
print("#######################################")

