Nevarro_Nummies=float(input("Nevarro Nummies consumidas(en unidades) :"))
Space_soup= int(input("Space soup consumida (en [ml]):"))
Carne_de_rana= int(input("Carne de rana consumida (en [g]):"))
carbo_nummies= 6.00*Nevarro_Nummies
carbo_space_soup= (12/285)*Space_soup
carbo_carne_rana= 0*Carne_de_rana
grasas_nummies= 1.90*Nevarro_Nummies
grasas_space_soup=(10/285)*Space_soup
grasas_carne_rana=(0.3/100)*Carne_de_rana
prot_nummies= 0.8*Nevarro_Nummies
prot_space_soup= (11/285)*Space_soup
prot_carne_rana= (16/100)*Carne_de_rana
Carbohidratos= round(carbo_nummies + carbo_space_soup + carbo_carne_rana,2)
Grasas= round(grasas_nummies + grasas_space_soup + grasas_carne_rana,2)
Proteinas= round(prot_nummies + prot_space_soup + prot_carne_rana,2)
Calorias= round(4*Carbohidratos + 9*Grasas + 4*Proteinas)
print("Grogu ha consumido:")
print(Carbohidratos,"[g] de carbohidratos")                        
print(Grasas,"[g] de grasas") 
print(Proteinas,"[g] de proteinas")
print("Que nos da un total de:")
print(Calorias,"[calorias]")
 
'''
#usando el ejemplo del pdf de la tarea
Nevarro Nummies consumidas(en unidades) :1.5 
Space soup consumida (en [ml]):420
Carne de rana consumida (en [g]):210
Grogu ha consumido:
#carbohidratos totales
26.68 [g] de carbohidratos
#grasas totales
18.22 [g] de grasas           
#proteinas totales
51.01 [g] de proteinas
Que nos da un total de:
475 [calorias]
'''
'''
# usando valores propios (NN=2,Ss=510,CR=230)
  Nevarro Nummies consumidas(en unidades) :2
Space soup consumida (en [ml]):510
Carne de rana consumida (en [g]):230
Grogu ha consumido:
#Carbohidratos totales
33.47 [g] de carbohidratos
#grasas totales
22.38 [g] de grasas
#proteinas totales
58.08 [g] de proteinas
Que nos da un total de:
568 [calorias] 
   '''
'''
# use los valores NN= 4,Ss=650,CR=150

Nevarro Nummies consumidas(en unidades) :4
Space soup consumida (en [ml]):650
Carne de rana consumida (en [g]):150
Grogu ha consumido:
#Carbohidratos totales
51.37 [g] de carbohidratos
#Grasas totales
30.86 [g] de grasas
#Proteinas totales
52.29 [g] de proteinas
Que nos da un total de:
692 [calorias]
'''
