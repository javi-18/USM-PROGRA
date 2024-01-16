Local1=input("Nombre surcursal:")
cor_x1=int(input("Coordenada x:"))
cor_y1=int(input("Coordenda y:"))
Local2=input("Nombre sucursal:")
cor_x2=int(input("Coordenada x:"))
cor_y2=int(input("Coordenada y:"))
Local3=input("Nombre sucursal:")
cor_x3=int(input("Coordenada x:"))
cor_y3=int(input("Coordenada y:"))
menor= float("inf")
a="si"
total=0
seguir=True
pedidos=0
cont1=0
cont2=0
cont3=0
valor_car= 4000
valor_veget= 3000
valor_veg= 3500
from math import sqrt
while a=="si"and seguir==True:
    plato=int(input("Ingrese numero de plato:"))
    if plato==-1:
        seguir=False
        a="no"
    
        while plato!=-1:
             if plato==1:
                total=total+valor_car
                cont1=cont1+1
            
             elif plato==2:
                 total=total+ valor_veget
                 cont2=cont2+1
             
             else:
                 total=total + valor_veg
                 cont3=cont3+1
    
   
            
    print("Total del pedido $",total)
        
    coordenda_X=int(input("Ingrese coordenda x cliente:"))
    coordenada_Y=int(input("Ingrese coordenada y cliente:"))
    distancia1=sqrt((cor_x1 - coordenda_X)**2 +(cor_y1- coordenada_Y)**2)
    distancia2= sqrt((cor_x2 - coordenda_X)**2 + (cor_y2- coordenada_Y)**2)
    distancia3= sqrt((cor_x3 - coordenda_X)**2 + (cor_y3- coordenada_Y)**2)
    if distancia1 < menor:
        menor= distancia1
        print("Pedido sera entregado por",Local1)
        
    
    elif distancia2 < menor:
        menor=distancia2
        print("Pedido sera entregado por",Local2)
        
    else:
        menor=distancia3
        print("Pedido sera entregado por",Local3)
    
    if a=="si":  
        input("¿Desea registrar otro pedido?:")
        seguir=True
    else:
       
        input("¿Deses registrar otro pedido?:")
        seguir= False
    print()
    
print("####Estadisticas Finales####")
print("Monto total recaudado $",total)
print(Local1,"entrego",cont1,"pedidos")
print(Local2,"entrego",cont2,"pedidos")
print(Local3,"entrego",cont3,"pedidos")    
